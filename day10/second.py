with open("input.txt") as inp:
    adapters = list(map(lambda line: int(line), inp.readlines()))

adapters.sort()
end = adapters[-1] + 3
adapters.append(end)
adapter_arrangements_dictionary = dict.fromkeys(adapters)


def find_possible_arrangements(current_adapter):
    if current_adapter == end:
        return 1
    possible_next_adapters = {jolts if jolts in adapters else None
                              for jolts in range(current_adapter + 1, current_adapter + 4)}
    possible_next_adapters.discard(None)
    if not possible_next_adapters:
        return 0

    num_arrangements = 0
    for next_adapter in possible_next_adapters:
        num_arrangements += adapter_arrangements_dictionary[next_adapter]
    return num_arrangements


adapters.reverse()
for adapter in adapters:
    adapter_arrangements_dictionary[adapter] = find_possible_arrangements(adapter)

print(find_possible_arrangements(0))
# >>> 193434623148032
