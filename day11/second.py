with open("input.txt") as inp:
    seats = inp.read().split("\n")

seats.pop()
prev_seats = seats.copy()
changes = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)]
end_num_occupied = 0


def check_empty(row_index, col_index):
    for row_change, col_change in changes:
        current_row, current_col = row_index, col_index
        while 0 <= current_row + row_change < len(seats) \
                and 0 <= current_col + col_change < len(seats[0]):
            current_row += row_change
            current_col += col_change
            if prev_seats[current_row][current_col] == '#':
                return False
            elif prev_seats[current_row][current_col] == 'L':
                break
    return True


def check_occupied(row_index, col_index):
    num_occupied = 0
    for row_change, col_change in changes:
        current_row, current_col = row_index, col_index
        while 0 <= current_row + row_change < len(seats) \
                and 0 <= current_col + col_change < len(seats[0]):
            current_row += row_change
            current_col += col_change
            if prev_seats[current_row][current_col] == '#':
                num_occupied += 1
                break
            elif prev_seats[current_row][current_col] == 'L':
                break
        if num_occupied == 5:
            return True
    return False


while True:
    prev_seats = seats.copy()
    print("\n")
    for i in range(len(seats) * len(seats[0])):
        row = i // len(seats[0])
        col = i % len(seats[0])
        if seats[row][col] == 'L' and check_empty(row, col):
            seats[row] = seats[row][:col] + '#' + seats[row][col + 1:]
        elif seats[row][col] == '#' and check_occupied(row, col):
            seats[row] = seats[row][:col] + 'L' + seats[row][col + 1:]
    if prev_seats == seats:
        break

for seat_row in seats:
    for char in seat_row:
        if char == '#':
            end_num_occupied += 1

print(f"{end_num_occupied = }")
# >>> end_num_occupied = 1995
