with open("input.txt") as inp:
    instructions = inp.read().split('\n')[:-1]

wp_horiz_pos = 10
wp_vert_pos = 1
ship_horiz_pos = 0
ship_vert_pos = 0


def rotate(horizontal, vertical, degrees, ccw):
    if degrees == 270:
        degrees -= 180
        ccw = not ccw
    if degrees == 90:
        if ccw:
            return vertical * -1, horizontal
        else:
            return vertical, horizontal * -1
    elif degrees == 180:
        return horizontal * -1, vertical * -1


for instruction in instructions:
    instruction_type = instruction[:1]
    instruction_amount = int(instruction[1:])
    if instruction_type == 'N':
        wp_vert_pos += instruction_amount
    elif instruction_type == 'E':
        wp_horiz_pos += instruction_amount
    elif instruction_type == 'S':
        wp_vert_pos -= instruction_amount
    elif instruction_type == 'W':
        wp_horiz_pos -= instruction_amount
    elif instruction_type == 'F':
        ship_horiz_pos += instruction_amount * wp_horiz_pos
        ship_vert_pos += instruction_amount * wp_vert_pos
    elif instruction_type == 'R':
        wp_horiz_pos, wp_vert_pos = rotate(wp_horiz_pos, wp_vert_pos, instruction_amount, False)
    else:
        wp_horiz_pos, wp_vert_pos = rotate(wp_horiz_pos, wp_vert_pos, instruction_amount, True)

print(abs(ship_horiz_pos) + abs(ship_vert_pos))
# >>> 58606
