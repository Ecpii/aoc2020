from first import list_rules, messages


def validate(message: str) -> bool:
    """ only works for rule 0 """

    if len(message) % 8 != 0:
        return False
    number_of_42s = 0
    number_of_31s = 0
    done_with_42s = False
    valid_42_strings = set(list_rules['42'])
    valid_31_strings = set(list_rules['31'])

    while message:
        current_slice = message[:8]
        if current_slice not in valid_42_strings | valid_31_strings:
            return False
        if not done_with_42s and current_slice in valid_42_strings:
            number_of_42s += 1
        elif done_with_42s and current_slice in valid_31_strings:
            number_of_31s += 1
        elif not done_with_42s and current_slice in valid_31_strings:
            done_with_42s = True
            number_of_31s += 1
        else:
            return False
        message = message[8:]
    return number_of_42s > number_of_31s != 0


num_valid_messages = 0
for sent_message in messages:
    if validate(sent_message):
        num_valid_messages += 1
print(num_valid_messages)
# >>> 332
