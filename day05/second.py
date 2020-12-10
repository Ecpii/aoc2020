def get_row(input_ticket):
    input_ticket_rows = input_ticket[:7]
    output = ''
    for letter in input_ticket_rows:
        output += "0" if letter == "F" else "1"

    return int(output, 2)


def get_col(input_ticket):
    input_ticket_cols = input_ticket[7:]
    output = ''
    for letter in input_ticket_cols:
        output += "0" if letter == "L" else "1"

    return int(output, 2)


def get_id(input_ticket):
    return 8 * get_row(input_ticket) + get_col(input_ticket)


boarding_tickets = open("input.txt", "rt").read().split("\n")
boarding_tickets.pop()

possible_ticket_ids = set([i for i in range(1024)])

for boarding_ticket in boarding_tickets:
    current_ticket_id = get_id(boarding_ticket)
    possible_ticket_ids.remove(current_ticket_id)

for ticket_id in possible_ticket_ids:
    if ticket_id - 1 in possible_ticket_ids:
        continue
    if ticket_id + 1 in possible_ticket_ids:
        continue
    print(ticket_id)
