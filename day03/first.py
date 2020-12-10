file_contents = open("input.txt", "rt")
hill = file_contents.read().split("\n")

trees_encountered = 0
section_length = len(hill[0])

for row in range(1, len(hill) - 1):
    col = row * 3 % section_length
    print(f"{row = }")
    print(f"{col = }")
    if hill[row][col] == '#':
        trees_encountered += 1
print(trees_encountered)
