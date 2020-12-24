from collections import deque

input_order = '562893147'
# input_order = '389125467'
cup_circle = deque(map(lambda digit: int(digit), input_order))


def crab_pick_up():
    current_cup = cup_circle.popleft()
    picked_up_cups = deque()
    invalid_destinations = set()
    invalid_destinations.add(0)
    for i in range(3):
        picked_up_cup = cup_circle.popleft()
        invalid_destinations.add(picked_up_cup)
        picked_up_cups.append(picked_up_cup)

    destination_cup = current_cup - 1
    while destination_cup in invalid_destinations:
        if destination_cup <= 1:
            destination_cup = len(input_order)
        else:
            destination_cup -= 1

    drive_by_cups = deque()
    while not drive_by_cups or destination_cup != drive_by_cups[-1]:
        drive_by_cups.append(cup_circle.popleft())
    for i in range(3):
        cup_circle.appendleft(picked_up_cups.pop())
    for i in range(len(drive_by_cups)):
        cup_circle.appendleft(drive_by_cups.pop())
    cup_circle.appendleft(current_cup)
    cup_circle.rotate(-1)


for move in range(100):
    print(f'\n-- move {move + 1} --')
    crab_pick_up()
    print(f'cups: {cup_circle}')

while cup_circle[0] != 1:
    cup_circle.rotate(-1)
cup_circle.popleft()

for cup in cup_circle:
    print(cup, end='')
# >>> 38925764
