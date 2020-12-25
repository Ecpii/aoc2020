# public_keys = [5764801, 17807724]
public_keys = [8335663, 8614349]


def transform_subject(subject_num: int, loop_size: int):
    public_key = 1
    for i in range(loop_size):
        public_key *= subject_num
        public_key %= 20201227  # wait is this a date
    return public_key


def reverse_transform(key: int):
    num_rounds = 0
    while key != 1:
        if not key % 7:
            key /= 7
            num_rounds += 1
        else:
            key += 20201227

    return num_rounds


def find_encryption_key():
    prefer_card_loop_size = loop_sizes[0] < loop_sizes[1]
    if prefer_card_loop_size:
        encryption_subject = public_keys[1]
        encryption_loop_size = loop_sizes[0]
    else:
        encryption_subject = public_keys[0]
        encryption_loop_size = loop_sizes[1]

    encryption_key = transform_subject(encryption_subject, encryption_loop_size)
    print(encryption_key)


loop_sizes = [None, None]
for j in range(2):
    potential_loop_size = reverse_transform(public_keys[j])
    print(f'{str(j + 1) + ("nd" if j else "st")} loop size: {potential_loop_size}')
    loop_sizes[j] = potential_loop_size

find_encryption_key()
# >>> 6408263
