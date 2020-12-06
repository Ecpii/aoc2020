file_contents = open("input.txt", "rt")
hill = file_contents.read().split("\n")
section_length = len(hill[0])


def count_trees(slopex, slopey):
    trees_encountered = 0
    for row in range(slopey, len(hill) - 1, slopey):
        col = int(row / slopey * slopex % section_length)
        print(f"{row = }")
        print(f"{col = }")
        if hill[row][col] == '#':
            trees_encountered += 1
    return trees_encountered


print(count_trees(3, 1))
