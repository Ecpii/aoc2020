with open("input.txt") as inp:
    data = inp.readlines()


def apply_mask(number, bit_mask):
    for i in range(len(bit_mask)):
        if bit_mask[i] == 'X':
            continue
        if bit_mask[i] == '0' and number & 2 ** (35 - i):
            number -= 2 ** (35 - i)
        elif bit_mask[i] == '1' and not number & 2 ** (35 - i):
            number += 2 ** (35 - i)
    return number


mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
memory_dictionary = {}

for instruction in data:
    if instruction[:3] == "mas":
        mask = instruction[-37:-1]
        continue
    split_instruction = instruction.split("] = ")
    index = int(split_instruction[0][4:])
    value = int(split_instruction[1][:-1])
    memory_dictionary[index] = apply_mask(value, mask)

value_sum = 0
for address in memory_dictionary:
    value_sum += memory_dictionary[address]

print(value_sum)
# >>> 7440382076205
