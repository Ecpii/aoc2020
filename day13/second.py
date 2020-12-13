with open("testinput6.txt") as inp:
    inp.readline()
    raw_bus_ids = inp.readline()[:-1].split(',')

max_bus_id = 0
max_bus_index = 0
relative_bus_id_dict = dict()

for raw_bus_id in raw_bus_ids:
    try:
        if int(raw_bus_id) > max_bus_id:
            max_bus_id = int(raw_bus_id)
            max_bus_index = raw_bus_ids.index(raw_bus_id)
    except ValueError:
        continue

for i in range(len(raw_bus_ids)):
    if raw_bus_ids[i] != 'x':
        relative_bus_id_dict[int(raw_bus_ids[i])] = i - max_bus_index


def check_other_times(timestamp):
    for bus_id in relative_bus_id_dict:
        if (timestamp // bus_id + (1 if relative_bus_id_dict[bus_id] > 0 else 0)) * bus_id \
                - timestamp != relative_bus_id_dict[bus_id]:
            return False
    return True


possible_time = 0
while True:
    possible_time += max_bus_id
    if check_other_times(possible_time):
        break

print(possible_time - max_bus_index)
