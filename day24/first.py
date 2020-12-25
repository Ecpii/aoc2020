with open('testinput.txt') as inp:
    instructions = inp.read().split('\n')[:-1]


class Tile:
    num_black_tiles: int = 0
    offset_map: dict = {
        'e': (0, 2),
        'se': (1, 1),
        'sw': (1, -1),
        'w': (0, -2),
        'nw': (-1, -1),
        'ne': (-1, 1),
    }
    grid: dict = {
        0: {
            0: None
        }
    }

    @classmethod
    def pretty_print(cls):
        min_y = min(cls.grid)
        max_y = max(cls.grid)
        min_x = 0
        max_x = 0
        for y in cls.grid:
            if min(cls.grid[y]) < min_x:
                min_x = min(cls.grid[y])
            if max(cls.grid[y]) > max_x:
                max_x = max(cls.grid[y])

        max_y_length = max(len(str(min_y)), len(str(max_y)))
        max_x_length = max(len(str(min_x)), len(str(max_x)))
        x_reference_numbers = [f'{num: {max_x_length}}' for num in range(min_x, max_x + 1)]

        # first row for the reference numbers
        for i in range(max_x_length):
            print(' ' * (max_y_length + 2), end='')
            for reference_num in x_reference_numbers:
                print(reference_num[i], end=' ')
            print()

        # other rows
        for y in range(min_y, max_y + 1):
            y_is_even = not y % 2
            print(f'{y: {max_y_length}}', end=(' ' if y_is_even else '   '))
            if y in cls.grid:
                for x in range(min_x, max_x + 1):
                    if x in cls.grid[y]:
                        print('\033[1;30;47m . ' if cls.grid[y][x].is_white else '\033[1;37;40m # ',
                              end='\033[1;0;0m ')
                    elif (x + int(not y_is_even)) % 2 == 0:
                        print('\033[1;30;42m _ ', end='\033[1;0;0m ')
                print()
        print(f'Number of black tiles: {cls.num_black_tiles}')

    def __init__(self, y, x) -> None:
        self.is_white: bool = True
        self.y = y
        self.x = x

    def direction_to_coords(self, direction: str) -> tuple:
        end_y = self.y + Tile.offset_map[direction][0]
        end_x = self.x + Tile.offset_map[direction][1]
        return end_y, end_x

    def create_neighbor(self, direction: str) -> None:
        new_y, new_x = self.direction_to_coords(direction)
        new_neighbor = Tile(new_y, new_x)
        if new_y in Tile.grid:
            Tile.grid[new_y][new_x] = new_neighbor
        else:
            Tile.grid[new_y] = {new_x: new_neighbor}

    def get_neighbor(self, direction: str):
        new_y, new_x = self.direction_to_coords(direction)
        try:
            return Tile.grid[new_y][new_x]
        except KeyError:
            return None

    def flip(self) -> None:
        if self.is_white:
            Tile.num_black_tiles += 1
            self.is_white = False
        else:
            Tile.num_black_tiles -= 1
            self.is_white = True

    def follow_chain(self, directions: str) -> None:
        if not directions:
            self.flip()
            return

        current_direction = ''
        while current_direction not in Tile.offset_map:
            current_direction += directions[0]
            directions = directions[1:]

        if not self.get_neighbor(current_direction):
            self.create_neighbor(current_direction)
        target_neighbor = self.get_neighbor(current_direction)
        target_neighbor.follow_chain(directions)


starting_tile = Tile(0, 0)
Tile.grid[0][0] = starting_tile
for instruction in instructions:
    starting_tile.follow_chain(instruction)

# Tile.pretty_print()
# >>> 528
