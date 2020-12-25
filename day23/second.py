cups = {}


class Cup:
    # just a linked list but bad
    def __init__(self, next_label, label):
        self.next_label = next_label
        self.label = label


def crab_move():
    picked_up_labels = set()
    selected_cup = cups[current_label]
    first_picked_cup = cups[selected_cup.next_label]
    for j in range(3):
        selected_cup = cups[selected_cup.next_label]
        picked_up_labels.add(selected_cup.label)

    destination_label = current_label - 1
    while destination_label in picked_up_labels or destination_label < 1:
        if destination_label > 1:
            destination_label -= 1
        else:
            destination_label = 1000000

    destination_cup = cups[destination_label]
    cups[current_label].next_label = cups[selected_cup.next_label].label
    selected_cup.next_label = cups[destination_cup.next_label].label
    destination_cup.next_label = first_picked_cup.label


input_order = '562893147'
for i in range(len(input_order) - 1):
    digit = int(input_order[i])
    cups[digit] = Cup(int(input_order[i + 1]), digit)
cups[int(input_order[-1])] = Cup(10, int(input_order[-1]))

for i in range(10, 1000001):
    cups[i] = Cup(i + 1, i)
cups[1000000].next_label = cups[int(input_order[0])].label

current_label = int(input_order[0])
for i in range(10000000):
    crab_move()
    current_label = cups[current_label].next_label

print(cups[cups[1].next_label].label)
print(cups[cups[1].next_label].next_label)
print(cups[cups[1].next_label].label * cups[cups[1].next_label].next_label)
# >>> 131152940564
