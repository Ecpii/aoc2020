with open("testinput.txt") as inp:
    earliest_time = int(inp.readline()[:-1])
    raw_bus_ids = inp.readline()[:-1].split(',')

bus_ids = {int(bus_id) if bus_id != 'x' else 'x' for bus_id in raw_bus_ids}
bus_ids.discard('x')
earliest_bus_time = float('inf')
earliest_bus_id = 0

for bus_id in bus_ids:
    if earliest_time % bus_id != 0:
        first_departure = (earliest_time // bus_id + 1) * bus_id
        if first_departure < earliest_bus_time:
            earliest_bus_time = first_departure
            earliest_bus_id = bus_id
    else:
        earliest_bus_id = bus_id
        earliest_bus_time = earliest_time

print(earliest_bus_id * (earliest_bus_time - earliest_time))
