with open("input.txt") as inp:
    data = inp.readlines()
memory_dictionary = {}


def apply_mask(address, bit_mask):
    if 'X' not in bit_mask:
        return {address | int(bit_mask, 2)}
    # returns addresses
    addresses = set()

    i = bit_mask.index('X')
    next_bit_mask = bit_mask[:i] + '0' + bit_mask[i + 1:]
    addresses = addresses.union(apply_mask(address, next_bit_mask))
    addresses = addresses.union(apply_mask(address ^ (1 << (35 - i)), next_bit_mask))
    return addresses


mask = 'f'  # placeholder, mask is always assigned in data
for instruction in data:
    if instruction[1] == "a":
        mask = instruction[-37:-1]
        continue
    split_instruction = instruction.split("] = ")
    index = int(split_instruction[0][4:])
    value = int(split_instruction[1][:-1])
    assign_addresses = apply_mask(index, mask)
    for address in assign_addresses:
        memory_dictionary[address] = value

memory_sum = 0
for key in memory_dictionary:
    memory_sum += memory_dictionary[key]
print(memory_sum)
# >>> 4200656704538
