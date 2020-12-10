instructions = open("input.txt").readlines()


def find_end(instruction_index, accumulator, visited_instructions, can_branch):
    if instruction_index == len(instructions):
        return accumulator
    if instruction_index in visited_instructions:
        return
    visited_instructions.add(instruction_index)
    current_instruction = instructions[instruction_index][:3]
    current_argument = int(instructions[instruction_index][4:])

    if current_instruction == "acc":
        accumulator += current_argument
        possible_end_accumulator = find_end(instruction_index + 1, accumulator,
                                            visited_instructions, can_branch)
    elif current_instruction == "jmp":
        possible_end_accumulator = find_end(instruction_index + current_argument, accumulator,
                                            visited_instructions, can_branch)
        if possible_end_accumulator:
            return possible_end_accumulator
        if can_branch:
            possible_end_accumulator = find_end(instruction_index + 1, accumulator,
                                                visited_instructions, False)
    else:
        possible_end_accumulator = find_end(instruction_index + 1, accumulator,
                                            visited_instructions, can_branch)
        if possible_end_accumulator:
            return possible_end_accumulator
        if can_branch:
            possible_end_accumulator = find_end(instruction_index + 1, accumulator,
                                                visited_instructions, False)
    return possible_end_accumulator


print(find_end(0, 0, set(), True))
# > 1375
