with open("input.txt") as inp:
    seats = inp.read().split("\n")

seats.pop()
changes = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)]
end_num_occupied = 0


def check_empty(row_index, col_index, occupied):
    num_occupied = 0
    for row_change, col_change in changes:
        try:
            if row_index + row_change < 0 or col_index + col_change < 0:
                continue
            if prev_seats[row_index + row_change][col_index + col_change] == "#":
                num_occupied += 1
            if num_occupied == (4 if occupied else 1):
                return False
        except IndexError:
            continue
    return True


while True:
    prev_seats = seats.copy()
    for i in range(len(seats) * len(seats[0])):
        row = i // len(seats[0])
        col = i % len(seats[0])
        # this code is slow but i can't be bothered to change it
        if seats[row][col] == 'L' and check_empty(row, col, False):
            seats[row] = seats[row][:col] + '#' + seats[row][col + 1:]
        elif seats[row][col] == '#' and not check_empty(row, col, True):
            seats[row] = seats[row][:col] + 'L' + seats[row][col + 1:]
    if prev_seats == seats:
        break

for seat_row in seats:
    end_num_occupied += seat_row.count("#")

print(end_num_occupied)
# >>> 2211
