with open("input.txt") as inp:
    inp.readline()
    raw_bus_ids = inp.readline()[:-1].split(',')

bus_ids = []

for raw_bus_id in raw_bus_ids:
    try:
        bus_ids.append(int(raw_bus_id))
    except ValueError:
        bus_ids.append(raw_bus_id)


def check_other_times(timestamp):
    for i in range(1, len(bus_ids)):
        bus_id = bus_ids[i]
        if bus_id == 'x':
            continue
        if (timestamp // bus_id + (1 if timestamp % bus_id != 0 else 0)) \
                * bus_id % timestamp != i:
            return False
    return True


possible_time = 100000000000000 // bus_ids[0] * bus_ids[0]
while True:
    possible_time += bus_ids[0]
    if check_other_times(possible_time):
        break

print(possible_time)
