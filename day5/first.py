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
max_seat_id = -1

for boarding_ticket in boarding_tickets:
    current_ticket_id = get_id(boarding_ticket)
    if current_ticket_id > max_seat_id:
        max_seat_id = current_ticket_id

print(max_seat_id)
