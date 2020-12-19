with open('input.txt') as inp:
    hw_problems = inp.readlines()


def find_matching_paren(expression):
    curr_depth = 0
    for curr_index in range(len(expression)):
        if expression[curr_index] == '(':
            curr_depth += 1
        elif expression[curr_index] == ')':
            curr_depth -= 1
        if curr_depth == 0:
            return curr_index


def find_multi_stop(expression):
    curr_depth = 0
    curr_index = 0
    for curr_index in range(len(expression)):
        if expression[curr_index] == '(':
            curr_depth += 1
        elif expression[curr_index] == ')':
            curr_depth -= 1
        elif curr_depth == 0:
            if expression[curr_index] == '*':
                return curr_index - 1
    return curr_index + 1


def evaluate_exp(problem, operation='(', accumulator=0):
    if ' ' not in problem:
        if operation == '+':
            return accumulator + int(problem)
        else:
            if accumulator == 0:
                return int(problem)
            return accumulator * int(problem)

    if operation == '*':
        accumulator *= evaluate_exp(problem[:find_multi_stop(problem)])
    else:
        if problem[0] == '(':
            next_num = evaluate_exp(problem[1:find_matching_paren(problem)])
        else:
            next_num = int(problem[:problem.index(' ')])

        if operation == '+':
            accumulator += next_num
        else:
            accumulator = next_num

    if problem[0] == '(':
        next_problem = problem[find_matching_paren(problem) + 2:]
        if operation == '*':
            next_problem = problem[find_multi_stop(problem) + 1:]
        if not next_problem:
            return accumulator
    elif operation == '*':
        next_problem = problem[find_multi_stop(problem) + 1:]
        if not next_problem:
            return accumulator
    else:
        next_problem = problem[problem.index(' ') + 1:]

    next_operation = next_problem[0]
    next_problem = next_problem[next_problem.index(' ') + 1:]
    return evaluate_exp(next_problem, next_operation, accumulator)


problems_sum = 0
for hw_problem in hw_problems:
    problems_sum += evaluate_exp(hw_problem[:-1])
print(problems_sum)
# >>> 119224703255966
