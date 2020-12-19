with open('input.txt') as inp:
    hw_problems = inp.readlines()


def find_matching_paren(expression):
    curr_depth = 1
    curr_index = 0
    expression = expression[1:]
    while curr_depth != 0:
        curr_index += 1
        if '(' in expression:
            next_opening_paren_index = expression.index('(')
        else:
            next_opening_paren_index = 99
        if ')' in expression:
            next_closing_paren_index = expression.index(')')
        else:
            next_closing_paren_index = 99
        if next_opening_paren_index < next_closing_paren_index:
            curr_depth += 1
            curr_index += next_opening_paren_index
            expression = expression[next_opening_paren_index + 1:]
        else:
            curr_depth -= 1
            curr_index += next_closing_paren_index
            expression = expression[next_closing_paren_index + 1:]
    return curr_index


def evaluate_exp(problem, operation, accumulator):
    if ' ' not in problem:
        if operation == '+':
            return accumulator + int(problem)
        else:
            return accumulator * int(problem)
    if problem[0] == '(':
        next_num = evaluate_exp(problem[1:find_matching_paren(problem)], '(', 0)
    else:
        next_num = int(problem[:problem.index(' ')])
    if operation == '+':
        accumulator += next_num
    elif operation == '*':
        accumulator *= next_num
    else:
        accumulator = next_num

    if problem[0] == '(':
        next_problem = problem[find_matching_paren(problem) + 2:]
        if not next_problem:
            return accumulator
    else:
        next_problem = problem[problem.index(' ') + 1:]

    next_operation = next_problem[0]
    next_problem = next_problem[next_problem.index(' ') + 1:]
    return evaluate_exp(next_problem, next_operation, accumulator)


problems_sum = 0
for hw_problem in hw_problems:
    problems_sum += evaluate_exp(hw_problem[:-1], '+', 0)
print(problems_sum)
# >>> 1402255785165
