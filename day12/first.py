with open("input.txt") as inp:
    instructions = inp.read().split('\n')[:-1]

horizontal_pos = 0
vertical_pos = 0
# North, East, South, West
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
current_direction = 1

for instruction in instructions:
    instruction_type = instruction[:1]
    instruction_amount = int(instruction[1:])
    if instruction_type == 'N':
        vertical_pos += instruction_amount
    elif instruction_type == 'E':
        horizontal_pos += instruction_amount
    elif instruction_type == 'S':
        vertical_pos -= instruction_amount
    elif instruction_type == 'W':
        horizontal_pos -= instruction_amount
    elif instruction_type == 'F':
        vertical_pos += instruction_amount * directions[current_direction][1]
        horizontal_pos += instruction_amount * directions[current_direction][0]
    elif instruction_type == 'R':
        current_direction += instruction_amount // 90
        current_direction %= 4
    else:
        current_direction -= instruction_amount // 90
        current_direction %= 4

print(abs(horizontal_pos) + abs(vertical_pos))
# >>> 1631
