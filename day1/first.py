def check_triple_sum(path, number):
    data = open(path, mode='rt')
    data_contents = data.read()
    data_contents_array = data_contents.split()
    numbers = [int(item) for item in data_contents_array]

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            k = number - numbers[i] - numbers[j]
            if k in numbers[j + 1:]:
                return k * numbers[j] * numbers[i]
    return 0


print(check_triple_sum('input.txt', 2020))
