with open("input.txt") as inp:
    adapters = list(map(lambda line: int(line), inp.readlines()))

adapters.sort()
adapters.append(adapters[len(adapters) - 1] + 3)
jolt_diff_distribution = [0, 0, 0]
current_jolts = 0

for adapter in adapters:
    difference = adapter - current_jolts
    jolt_diff_distribution[difference - 1] += 1
    current_jolts = adapter

print(jolt_diff_distribution[0] * jolt_diff_distribution[2])
# >>> 3000
