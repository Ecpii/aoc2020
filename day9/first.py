with open("input.txt") as inp:
    encrypted_file = inp.readlines()
encrypted_msg = [int(line) for line in encrypted_file]


def decode_xmas(preamble_size):
    previous_numbers = set(encrypted_msg[:preamble_size])

    for i in range(preamble_size, len(encrypted_msg)):
        valid_number = False
        current_number = encrypted_msg[i]
        for number in previous_numbers:
            if current_number - number in previous_numbers:
                valid_number = True
                break
        if not valid_number:
            return current_number
        previous_numbers.remove(encrypted_msg[i - preamble_size])
        previous_numbers.add(current_number)


print(decode_xmas(25))
