groups = open("input.txt", "rt").read().split("\n\n")
questions_sum = 0

for group in groups:
    raw_answers = group.replace("\n", "")
    unique_answers = set()
    for letter in raw_answers:
        unique_answers.add(letter)

    questions_sum += len(unique_answers)

print(questions_sum)
