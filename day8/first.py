instructions = open("input.txt").readlines()
current_instruction_index = 0
accumulator = 0
visited_instructions = set()

while current_instruction_index not in visited_instructions:
    visited_instructions.add(current_instruction_index)
    current_instruction = instructions[current_instruction_index][:3]

    if current_instruction == "nop":
        current_instruction_index += 1
        continue

    current_argument = int(instructions[current_instruction_index][4:])
    if current_instruction == "acc":
        current_instruction_index += 1
        accumulator += current_argument
    else:
        current_instruction_index += current_argument

print(accumulator)
# > 1548
