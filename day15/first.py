with open("input.txt") as inp:
    starting_instructions = inp.readline()[:-1].split(",")
numbers = list(map(lambda instruction: int(instruction), starting_instructions))
last_spoken_indices = {numbers[i]: i for i in range(len(numbers))}

for i in range(len(numbers) - 1, 2019):
    try:
        numbers.append(i - last_spoken_indices[numbers[i]])
    except KeyError:
        numbers.append(0)
    last_spoken_indices[numbers[i]] = i

print(numbers[-1])
# >>> 706
