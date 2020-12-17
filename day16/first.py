with open("input.txt") as inp:
    complete_file = inp.read()

out_file = open("valid_tickets.txt", "w")
file_sections = complete_file.split("\n\n")
rules = file_sections[0].split("\n")
tickets = file_sections[2].split("\n")[1:-1]
valid_values = set()
ticket_scan_err = 0


def parse_rule(rule):
    rule_ranges = rule[rule.index(":") + 2:].split(" or ")
    for rule_range in rule_ranges:
        start_index = int(rule_range[:rule_range.index('-')])
        end_index = int(rule_range[rule_range.index('-') + 1:]) + 1
        valid_values.update(range(start_index, end_index))


for rule in rules:
    parse_rule(rule)

for ticket in tickets:
    valid_ticket = True
    fields = ticket.split(',')
    for field in fields:
        if int(field) not in valid_values:
            valid_ticket = False
            ticket_scan_err += int(field)
    if valid_ticket:
        out_file.write(ticket + "\n")

out_file.close()
print(ticket_scan_err)
# >>> 19240