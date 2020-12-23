from first import tile_dict, tile_edges, edge_matches, find_edges

tile_length = 10
image_tile_length = int(len(tile_dict) ** .5)
image_length = (tile_length - 2) * image_tile_length


def rotate(tile_id: int, degrees: int) -> None:
    """Rotates a given tile counterclockwise in tile_dict given id and degrees (multiple of 90)"""
    if degrees == 0:
        return
    for j in range(degrees // 90):
        tile = tile_dict[tile_id]
        new_tile = ['' for _ in range(len(tile))]
        for row in tile:
            # builds each column from bottom to top, right to left of new tile
            # with each row from left to right, top to bottom
            for i in range(len(tile)):
                new_tile[len(tile) - 1 - i] += row[i]
        tile_dict[tile_id] = new_tile
    if tile_id != -1:
        # recalculate the edges of the rotated tile
        new_edge_matches = [None for _ in range(4)]
        for i in range(4):
            new_edge_matches[(i + degrees // 90) % 4] = edge_matches[tile_id][i]
        edge_matches[tile_id] = new_edge_matches
        find_edges(tile_id)


def flip_tile(tile_id: int, horizontal: bool) -> None:
    """Flips a tile with a given id and boolean to specify a horizontal or vertical flip"""
    if horizontal:
        for i in range(len(tile_dict[tile_id])):
            tile_dict[tile_id][i] = tile_dict[tile_id][i][::-1]
        indexes = (1, 3)
    else:
        tile_dict[tile_id].reverse()
        indexes = (0, 2)

    if tile_id != -1:
        # recalculate the edges of the flipped tile
        edge_matches[tile_id][indexes[0]], edge_matches[tile_id][indexes[1]] = \
            edge_matches[tile_id][indexes[1]], edge_matches[tile_id][indexes[0]]
        tile_edges[tile_id][indexes[0]], tile_edges[tile_id][indexes[1]], = \
            tile_edges[tile_id][indexes[1]], tile_edges[tile_id][indexes[0]]
        find_edges(tile_id)


# now unused function that was used for debugging and seeing each tile
def pretty_print(tile_id: int) -> None:
    """Prints a tile with coloring and information about its edges"""
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
    """Prints the final image with coloring as well as information about the water roughness"""
    print("\nFinal Image:")
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
    """Fills a row of the image with tile_ids, given that the row already has a tile_id
    in the beginning."""
    previous_tile_id = tile_orientation[row_num][-1]
    while edge_matches[previous_tile_id][3]:
        current_tile_id = edge_matches[previous_tile_id][3]
        # rotates the tile such that the matching sides are connected
        index_difference = 5 - edge_matches[current_tile_id].index(previous_tile_id)
        rotate(current_tile_id, index_difference * 90 % 360)

        # if they're connected in the wrong way, flip it vertically
        if tile_edges[current_tile_id][1] != tile_edges[previous_tile_id][3]:
            flip_tile(current_tile_id, False)

        tile_orientation[row_num].append(current_tile_id)
        previous_tile_id = tile_orientation[row_num][-1]


def orient_first_tile(row_num: int) -> None:
    """Rotates the first tile in a row to match the left edge and the tile above."""
    previous_row_start_id = tile_orientation[row_num - 1][0]
    first_tile_id = edge_matches[previous_row_start_id][2]
    index_difference = 4 - edge_matches[first_tile_id].index(previous_row_start_id)

    rotate(first_tile_id, index_difference * 90 % 360)
    if edge_matches[first_tile_id][1]:
        flip_tile(first_tile_id, True)
    tile_orientation[row_num].append(first_tile_id)


def assemble_image(orientation: list) -> list:
    """Uses an array of tile ids to create a string array representing the image."""
    final_image = ['' for _ in range(image_length)]
    for tile_row_num in range(image_tile_length):
        for tile_id in orientation[tile_row_num]:
            tile = tile_dict[tile_id][1:tile_length - 1]
            for row_num in range(len(tile)):
                final_image[row_num + (tile_length - 2) * tile_row_num] += \
                    tile[row_num][1:tile_length - 1]
    return final_image


def find_loch_ness(start_y: int, start_x: int) -> list:
    """Attempts to find a loch ness monster with the given starting coords
    (looks in the fourth quadrant relative to the starting coordinates)"""
    coordinates = list()
    for offset in loch_ness_pattern:
        if tile_dict[-1][start_y + offset[0]][start_x + offset[1]] in {'#', 'O'}:
            coordinates.append((start_y + offset[0], start_x + offset[1]))
        else:
            return []
    return coordinates


# an array to store the positions of each tile id
tile_orientation = [
    [] for i in range(image_tile_length)
]

# generates the first corner and rotates it correctly
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

# builds each row and assembles the image at the end, assigns it to id -1
for i in range(1, image_tile_length):
    orient_first_tile(i)
    build_row(i)
tile_dict[-1] = assemble_image(tile_orientation)

# generates the pattern from the loch ness string
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

# luckily, my pattern didn't need to be rotated or flipped, so code there is removed
# (but it's in a previous commit)
for y in range(len(tile_dict[-1]) - len(loch_ness)):
    for x in range(len(tile_dict[-1][0]) - len(loch_ness[0]) - 1):
        possible_loch_ness_coords = find_loch_ness(y, x)
        if possible_loch_ness_coords:
            for coord in possible_loch_ness_coords:
                tile_dict[-1][coord[0]] = tile_dict[-1][coord[0]][:coord[1]] + 'O' + \
                                          tile_dict[-1][coord[0]][coord[1] + 1:]

pretty_print_image()
# >>> 1649
