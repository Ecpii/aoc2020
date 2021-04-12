with open("input.txt") as inp:
    complete_file = inp.read()

file_sections = complete_file.split("\n\n")
rules = file_sections[0].split("\n")
my_ticket = file_sections[1].split("\n")[1].split(',')
tickets = file_sections[2].split("\n")[1:-1]
valid_tickets = []
valid_values = set()
ticket_scan_err = 0


def parse_rule(rule):
    rule_ranges = rule[rule.index(":") + 2:].split(" or ")
    current_rule_value_range = set()
    for rule_range in rule_ranges:
        start_index = int(rule_range[:rule_range.index('-')])
        end_index = int(rule_range[rule_range.index('-') + 1:]) + 1
        current_rule_value_range.update(range(start_index, end_index))
    return current_rule_value_range


for rule in rules:
    rule_value_range = parse_rule(rule)
    valid_values.update(rule_value_range)

for ticket in tickets:
    valid_ticket = True
    fields = ticket.split(',')
    for field in fields:
        if int(field) not in valid_values:
            valid_ticket = False
            ticket_scan_err += int(field)
    if valid_ticket:
        valid_tickets.append(ticket)

print(ticket_scan_err)
# >>> 19240
