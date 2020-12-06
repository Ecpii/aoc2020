groups = open("input.txt", "rt").read().split("\n\n")
questions_sum = 0

for group in groups:
    raw_answers = group.replace("\n", "")
    unique_answers = set(raw_answers)
    questions_sum += len(unique_answers)

print(questions_sum)
