with open("valid_tickets.txt") as inp:
    tickets = inp.readlines()
with open("input.txt") as inp:
    input_data = inp.read()

split_input_data = input_data.split("\n\n")
rules = split_input_data[0].split("\n")
my_ticket = split_input_data[1].split("\n")[1].split(",")
field_ranges = []
field_positions = []
determined_positions = set()

for rule in rules:
    current_value_range = set()
    rule_ranges = rule[rule.index(":") + 2:].split(" or ")
    for rule_range in rule_ranges:
        start_index = int(rule_range[:rule_range.index('-')])
        end_index = int(rule_range[rule_range.index('-') + 1:]) + 1
        current_value_range.update(range(start_index, end_index))
    field_ranges.append(current_value_range)

for field_range in field_ranges:
    possible_positions = set(range(0, len(rules))).difference(determined_positions)
    determined = False
    for ticket in tickets:
        ticket_fields = ticket[:-1].split(',')
        for i in range(len(ticket_fields)):
            if int(ticket_fields[i]) not in field_range:
                possible_positions.discard(i)
        if len(possible_positions) == 1:
            (determined_position,) = possible_positions
            determined_positions.add(determined_position)
            field_positions.append(determined_position)
            determined = True
            break
    if not determined:
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
