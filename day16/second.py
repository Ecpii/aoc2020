from first import valid_tickets as tickets, rules, my_ticket, parse_rule

field_ranges = []
field_positions = []
determined_positions = set()

for rule in rules:
    current_value_range = parse_rule(rule)
    field_ranges.append(current_value_range)

for field_range in field_ranges:
    possible_positions = set(range(0, len(rules))).difference(determined_positions)
    for ticket in tickets:
        ticket_fields = ticket.split(',')
        for i in range(len(ticket_fields)):
            if int(ticket_fields[i]) not in field_range:
                possible_positions.discard(i)
        if len(possible_positions) == 1:
            (determined_position,) = possible_positions
            determined_positions.add(determined_position)
            field_positions.append(determined_position)
            break
    else:
        field_positions.append(possible_positions)

while any(isinstance(field_position, set) for field_position in field_positions):
    for i in range(len(field_positions)):
        if isinstance(field_positions[i], set):
            field_positions[i] = field_positions[i].difference(determined_positions)
            if len(field_positions[i]) == 1:
                (determined_position,) = field_positions[i]
                determined_positions.add(determined_position)
                field_positions[i] = determined_position

product = 1
for i in range(6):
    product *= int(my_ticket[field_positions[i]])

print(product)
# >>> 21095351239483
