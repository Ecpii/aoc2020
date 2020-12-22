from first import tile_dict, tile_edges, edge_matches, find_edges

tile_length = 10
image_tile_length = int(len(tile_dict) ** .5)
image_length = tile_length * image_tile_length

tile_orientation = [
    [] for i in range(image_tile_length)
]


def rotate(tile_id: int, degrees: int) -> None:
    if degrees == 0:
        return
    for j in range(degrees // 90):
        tile = tile_dict[tile_id]
        new_tile = ['' for _ in range(tile_length)]
        for row in tile:
            for i in range(tile_length):
                new_tile[tile_length - 1 - i] += row[i]
        tile_dict[tile_id] = new_tile
    new_edge_matches = [None for _ in range(4)]
    for i in range(4):
        new_edge_matches[(i + degrees // 90) % 4] = edge_matches[tile_id][i]
    edge_matches[tile_id] = new_edge_matches
    find_edges(tile_id)


def flip_tile(tile_id: int, horizontal: bool) -> None:
    if horizontal:
        for i in range(tile_length):
            tile_dict[tile_id][i] = tile_dict[tile_id][i][::-1]
        indexes = (1, 3)
    else:
        tile_dict[tile_id].reverse()
        indexes = (0, 2)

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


def pretty_print_image(tile_id: int) -> None:
    print("\nAligned Image:")
    whole_image = tile_dict[tile_id]
    for line_num in range(image_length):
        if line_num % tile_length == 0:
            print(f'\033[1;30;107m')
        line = whole_image[line_num]
        for letter in line:
            if letter == '.':
                print(f'\033[1;30;0m{letter}', end=' ')
            elif letter == '#':
                print(f'\033[1;30;46m{letter}', end=' ')
            else:
                print(f'\033[1;30;107m{letter}', end=' ')
        print(f'\033[0;0;0m')


def build_row(row_num: int) -> None:
    previous_tile_id = tile_orientation[row_num][-1]
    while edge_matches[previous_tile_id][3]:
        next_tile_id = edge_matches[previous_tile_id][3]

        for instruction in tile_change_instructions:
            rotate(next_tile_id, instruction[0])
            if instruction[1]:
                flip_tile(next_tile_id, instruction[2])

            pretty_print(next_tile_id)
            if edge_matches[next_tile_id][1] == previous_tile_id:
                if row_num == 0 and not edge_matches[next_tile_id][0] or \
                        row_num in range(1, image_tile_length - 1) or \
                        row_num == image_tile_length - 1 and not edge_matches[next_tile_id][2]:
                    tile_orientation[row_num].append(next_tile_id)
                    break

            # if not a good orientation, revert changes
            rotate(next_tile_id, 360 - instruction[0])
            if instruction[1]:
                flip_tile(next_tile_id, instruction[2])
        previous_tile_id = tile_orientation[row_num][-1]


def orient_first_tile(row_num: int) -> None:
    previous_row_start_id = tile_orientation[row_num - 1][0]
    first_tile_id = edge_matches[previous_row_start_id][2]

    for instruction in tile_change_instructions:
        rotate(first_tile_id, instruction[0])
        if instruction[1]:
            flip_tile(first_tile_id, instruction[2])

        pretty_print(first_tile_id)

        if edge_matches[first_tile_id][0] == previous_row_start_id \
                and not edge_matches[first_tile_id][1]:
            tile_orientation[row_num].append(first_tile_id)
            return
        # if not a good orientation, revert changes
        rotate(first_tile_id, 360 - instruction[0])
        if instruction[1]:
            flip_tile(first_tile_id, instruction[2])


def build_image(orientation: list) -> list:
    final_image = ['' for _ in range(image_length)]
    for tile_row_num in range(image_tile_length):
        for tile_id in orientation[tile_row_num]:
            tile = tile_dict[tile_id]
            for row_num in range(tile_length):
                final_image[row_num + tile_length * tile_row_num] +=\
                    tile[row_num] + ' '
    return final_image


tile_change_instructions = [
    # (degrees, flip, horizontal)
    (0, False, False),
    (90, False, False),
    (180, False, False),
    (270, False, False),
    (0, True, False),
    (0, True, True),
    (90, True, False),
    (90, True, True)
]

first_corner_id = 0
for tile_id in edge_matches:
    if edge_matches[tile_id].count(None) == 2:
        first_corner_id = tile_id
        break

# rotate the first tile until the left and upper sides are the ones without matches
while edge_matches[first_corner_id][0] or edge_matches[first_corner_id][1]:
    rotate(first_corner_id, 90)
    pretty_print(first_corner_id)
tile_orientation[0].append(first_corner_id)
build_row(0)

for i in range(1, image_tile_length):
    orient_first_tile(i)
    build_row(i)

tile_dict[-1] = build_image(tile_orientation)
pretty_print_image(-1)
