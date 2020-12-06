groups = open("input.txt", "rt").read().split("\n\n")
questions_sum = 0

for group in groups:
    individuals_answers = group.split("\n")
    shared_answers = set(individuals_answers[0])
    if len(individuals_answers) == 1:
        questions_sum += len(shared_answers)
        continue

    for i in range(1, len(individuals_answers)):
        shared_answers = shared_answers.intersection(set(individuals_answers[i]))
    questions_sum += len(shared_answers)

print(questions_sum)
