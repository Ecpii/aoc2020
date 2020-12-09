with open("input.txt") as inp:
    encrypted_file = inp.readlines()
encrypted_msg = [int(line) for line in encrypted_file]


def find_range(index, number):
    range_sum = 0
    current_index = index
    while range_sum < number:
        range_sum += encrypted_msg[current_index]
        current_index += 1
    if range_sum == number:
        return encrypted_msg[index:current_index]


def find_encryption_weakness(number):
    possible_range = []
    for i in range(len(encrypted_msg)):
        possible_range = find_range(i, number)
        if possible_range:
            break
    return min(possible_range) + max(possible_range)


print(find_encryption_weakness(556543474))
