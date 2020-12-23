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
            tile = tile_dict[tile_id]
            for row_num in range(tile_length):
                final_image[row_num + tile_length * tile_row_num] +=\
                    tile[row_num] + ' '
    return final_image


first_corner_id = 0
for edge_tile_id in edge_matches:
    if edge_matches[edge_tile_id].count(None) == 2:
        first_corner_id = edge_tile_id
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
