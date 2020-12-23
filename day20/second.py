from first import tile_dict, tile_edges, edge_matches, find_edges

tile_length = 10
image_tile_length = int(len(tile_dict) ** .5)
image_length = (tile_length - 2) * image_tile_length

tile_orientation = [
    [] for i in range(image_tile_length)
]


def rotate(tile_id: int, degrees: int) -> None:
    if degrees == 0:
        return
    for j in range(degrees // 90):
        tile = tile_dict[tile_id]
        new_tile = ['' for _ in range(len(tile))]
        for row in tile:
            for i in range(len(tile)):
                new_tile[len(tile) - 1 - i] += row[i]
        tile_dict[tile_id] = new_tile
    if tile_id != -1:
        new_edge_matches = [None for _ in range(4)]
        for i in range(4):
            new_edge_matches[(i + degrees // 90) % 4] = edge_matches[tile_id][i]
        edge_matches[tile_id] = new_edge_matches
        find_edges(tile_id)


def flip_tile(tile_id: int, horizontal: bool) -> None:
    if horizontal:
        for i in range(len(tile_dict[tile_id])):
            tile_dict[tile_id][i] = tile_dict[tile_id][i][::-1]
        indexes = (1, 3)
    else:
        tile_dict[tile_id].reverse()
        indexes = (0, 2)

    if tile_id != -1:
        # switch the edges on the ends that are parallel to the axis of rotation/flipping
        edge_matches[tile_id][indexes[0]], edge_matches[tile_id][indexes[1]] = \
            edge_matches[tile_id][indexes[1]], edge_matches[tile_id][indexes[0]]
        tile_edges[tile_id][indexes[0]], tile_edges[tile_id][indexes[1]], = \
            tile_edges[tile_id][indexes[1]], tile_edges[tile_id][indexes[0]]
        find_edges(tile_id)


def pretty_print(tile_id: int) -> None:
    print(f"\nTile {tile_id}:")
    whole_tile = tile_dict[tile_id]
    for line in whole_tile:
        for letter in line:
            if letter == '.':
                print(f'\033[1;30;0m{letter}', end=' ')
            else:
                print(f'\033[1;30;46m{letter}', end=' ')
        print(f'\033[0;0;0m')
    print(f"{tile_edges[tile_id] = }")
    print(f"{edge_matches[tile_id] = }")


def pretty_print_image() -> None:
    print("\nAligned Image:")
    water_roughness = 0
    whole_image = tile_dict[-1]
    for line in whole_image:
        for letter in line:
            if letter == '.':
                print(f'\033[1;30;0m{letter}', end=' ')
            elif letter == '#':
                print(f'\033[1;30;46m{letter}', end=' ')
                water_roughness += 1
            else:
                print(f'\033[1;30;107m{letter}', end=' ')
        print(f'\033[0;0;0m')
    print(f"{water_roughness = }")


def build_row(row_num: int) -> None:
    previous_tile_id = tile_orientation[row_num][-1]
    while edge_matches[previous_tile_id][3]:
        current_tile_id = edge_matches[previous_tile_id][3]
        index_difference = 5 - edge_matches[current_tile_id].index(previous_tile_id)

        rotate(current_tile_id, index_difference * 90 % 360)
        if tile_edges[current_tile_id][1] != tile_edges[previous_tile_id][3]:
            flip_tile(current_tile_id, False)
        tile_orientation[row_num].append(current_tile_id)
        previous_tile_id = tile_orientation[row_num][-1]


def orient_first_tile(row_num: int) -> None:
    previous_row_start_id = tile_orientation[row_num - 1][0]
    first_tile_id = edge_matches[previous_row_start_id][2]
    index_difference = 4 - edge_matches[first_tile_id].index(previous_row_start_id)

    rotate(first_tile_id, index_difference * 90 % 360)
    if edge_matches[first_tile_id][1]:
        flip_tile(first_tile_id, True)
    tile_orientation[row_num].append(first_tile_id)


def build_image(orientation: list) -> list:
    final_image = ['' for _ in range(image_length)]
    for tile_row_num in range(image_tile_length):
        for tile_id in orientation[tile_row_num]:
            tile = tile_dict[tile_id][1:tile_length - 1]
            for row_num in range(len(tile)):
                final_image[row_num + (tile_length - 2) * tile_row_num] += \
                    tile[row_num][1:tile_length - 1]
    return final_image


def find_loch_ness(start_y: int, start_x: int) -> set:
    coordinates = set()
    for offset in loch_ness_pattern:
        if tile_dict[-1][start_y + offset[0]][start_x + offset[1]] in {'#', 'O'}:
            coordinates.add((start_y + offset[0], start_x + offset[1]))
        else:
            return set()
    return coordinates


first_corner_id = 0
for edge_tile_id in edge_matches:
    if edge_matches[edge_tile_id].count(None) == 2:
        first_corner_id = edge_tile_id
        break

# rotate the first tile until the left and upper sides are the ones without matches
while edge_matches[first_corner_id][0] or edge_matches[first_corner_id][1]:
    rotate(first_corner_id, 90)
tile_orientation[0].append(first_corner_id)
build_row(0)

for i in range(1, image_tile_length):
    orient_first_tile(i)
    build_row(i)

tile_dict[-1] = build_image(tile_orientation)

image_orientation_instructions = [
    (0, False, False),
    (90, False, False),
    (180, False, False),
    (270, False, False),
    (0, True, True),
    (0, True, False),
    (90, True, False),
    (90, True, True)
]

loch_ness = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
 """.split('\n')[1:]
loch_ness_pattern = []
for y in range(len(loch_ness)):
    for x in range(len(loch_ness[y])):
        if loch_ness[y][x] == '#':
            loch_ness_pattern.append((y, x))
loch_ness_coordinates = set()

for instruction in image_orientation_instructions:
    rotate(-1, instruction[0])
    if instruction[1]:
        flip_tile(-1, instruction[2])

    for y in range(len(tile_dict[-1]) - len(loch_ness)):
        for x in range(len(tile_dict[-1][0]) - len(loch_ness[0]) - 1):
            possible_loch_ness_coords = find_loch_ness(y, x)
            if possible_loch_ness_coords:
                for coord in possible_loch_ness_coords:
                    tile_dict[-1][coord[0]] = tile_dict[-1][coord[0]][:coord[1]] + 'O' + \
                                              tile_dict[-1][coord[0]][coord[1] + 1:]

    rotate(-1, 360 - instruction[0])
    if instruction[1]:
        flip_tile(-1, instruction[2])

pretty_print_image()
# >>> 1649
