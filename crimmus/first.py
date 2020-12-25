# public_keys = [5764801, 17807724]
public_keys = [8335663, 8614349]

transformed_subjects = {-1: 1}
flipped_transformed_subjects = {}


def transform_subject(subject_num: int, loop_size: int, override_start: bool = False):
    starting_point = max(transformed_subjects) + 1
    public_key = transformed_subjects[starting_point - 1]
    loop_range = range(starting_point, loop_size)
    if override_start:
        public_key = 1
        loop_range = range(loop_size)
    for i in loop_range:
        public_key *= subject_num
        public_key %= 20201227  # wait is this a date
        transformed_subjects[i] = public_key
        flipped_transformed_subjects[public_key] = i
    return public_key


def find_encryption_key():
    prefer_card_loop_size = loop_sizes[0] < loop_sizes[1]
    if prefer_card_loop_size:
        encryption_subject = public_keys[1]
        encryption_loop_size = loop_sizes[0]
    else:
        encryption_subject = public_keys[0]
        encryption_loop_size = loop_sizes[1]

    encryption_key = transform_subject(encryption_subject, encryption_loop_size, True)
    print(encryption_key)
    print(transformed_subjects)


loop_sizes = [None, None]
for j in range(2):
    potential_loop_size = max(transformed_subjects)
    while public_keys[j] not in flipped_transformed_subjects:
        potential_loop_size += 1
        transform_subject(7, potential_loop_size)
        # print(transformed_subjects)

    print('loop size: ' + str(potential_loop_size))
    loop_sizes[j] = potential_loop_size

find_encryption_key()
