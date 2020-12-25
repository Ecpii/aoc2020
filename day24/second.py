from first import Tile


def conway_day():
    black_neighbors = {}
    for y in Tile.grid:
        for x in Tile.grid[y]:
            if not Tile.grid[y][x].is_white:
                for direction in Tile.offset_map:
                    offset = Tile.offset_map[direction]
                    try:
                        black_neighbors[(y + offset[0], x + offset[1])] += 1
                    except KeyError:
                        black_neighbors[(y + offset[0], x + offset[1])] = 1
                try:
                    black_neighbors[(y, x)]
                except KeyError:
                    black_neighbors[(y, x)] = 0

    for coords in black_neighbors:
        num_nearby = black_neighbors[coords]
        try:
            current_tile = Tile.grid[coords[0]][coords[1]]
        except KeyError:
            current_tile = Tile(coords[0], coords[1])
            if coords[0] in Tile.grid:
                Tile.grid[coords[0]][coords[1]] = current_tile
            else:
                Tile.grid[coords[0]] = {coords[1]: current_tile}

        if (current_tile.is_white and num_nearby == 2) or \
                (not current_tile.is_white and (num_nearby == 0 or num_nearby in range(3, 7))):
            current_tile.flip()


for i in range(100):
    conway_day()
print(Tile.num_black_tiles)
# >>> 4200
