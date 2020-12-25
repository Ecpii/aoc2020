with open("input.txt") as inp:
    inp.readline()
    raw_bus_ids = inp.readline()[:-1].split(',')


def merge_buses(bus_1: tuple, bus_2: tuple):
    testing_time = bus_1[0]
    while (testing_time + bus_2[0]) % bus_2[1]:
        testing_time += bus_1[1]
    return testing_time % (bus_1[1] * bus_2[1]), bus_1[1] * bus_2[1]


bus_ids = [int(bus) if bus != 'x' else 'x' for bus in raw_bus_ids]

mega_bus = (0, bus_ids[0])
for i in range(1, len(bus_ids)):
    if bus_ids[i] != 'x':
        mega_bus = merge_buses(mega_bus, (i, bus_ids[i]))
print(mega_bus[0])
