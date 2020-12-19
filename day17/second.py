import copy

with open("input.txt") as inp:
    initial_state = inp.read().split("\n")[:-1]

neighbor_offsets = []
for w in range(-1, 2):
    for z in range(-1, 2):
        for y in range(-1, 2):
            for x in range(-1, 2):
                neighbor_offsets.append((w, z, y, x))
neighbor_offsets.remove((0, 0, 0, 0))

pocket_dim = {0: {0: {j: {i: True if initial_state[j][i] == '#' else False for i in range(
    len(initial_state[j]))} for j in range(len(initial_state))}}}


def pretty_print(dimension):
    num_active = 0
    min_w, min_z, min_y, min_x = 0, 0, 0, 0
    max_w, max_z, max_y, max_x = 0, 0, 0, 0
    for w_coord in dimension:
        if w_coord < min_w:
            min_w = w_coord
        elif w_coord > max_w:
            max_w = w_coord
        for z_coord in dimension[w_coord]:
            if z_coord < min_z:
                min_z = z_coord
            elif z_coord > max_z:
                max_z = z_coord
            for y_coord in dimension[w_coord][z_coord]:
                if y_coord < min_y:
                    min_y = y_coord
                elif y_coord > max_y:
                    max_y = y_coord
                for x_coord in dimension[w_coord][z_coord][y_coord]:
                    if x_coord < min_x:
                        min_x = x_coord
                    elif x_coord > max_x:
                        max_x = x_coord
    for l in range(min_w, max_w + 1):
        for k in range(min_z, max_z + 1):
            print(f"\nw = {l}, z = {k}")
            print(' ', *[abs(foo) for foo in range(min_x, max_x + 1)], sep=' ')
            for j in range(min_y, max_y + 1):
                print(f"{abs(j)}", end=' ')
                for i in range(min_x, max_x + 1):
                    try:
                        if dimension[l][k][j][i]:
                            print('#', end=' ')
                            num_active += 1
                        else:
                            print('.', end=' ')
                    except KeyError:
                        print('.', end=' ')
                print()
    print(f"{num_active = }")


for i in range(6):
    print(f"\n--- Round {i + 1} ---")
    active_neighbors = {}
    prev_pocket = copy.deepcopy(pocket_dim)
    for w in prev_pocket:
        for z in prev_pocket[w]:
            for y in prev_pocket[w][z]:
                for x in prev_pocket[w][z][y]:
                    if prev_pocket[w][z][y][x]:
                        try:
                            active_neighbors[(w, z, y, x)]
                        except KeyError:
                            active_neighbors[(w, z, y, x)] = 0

                        for neighbor_offset in neighbor_offsets:
                            new_w = w + neighbor_offset[0]
                            new_z = z + neighbor_offset[1]
                            new_y = y + neighbor_offset[2]
                            new_x = x + neighbor_offset[3]
                            try:
                                active_neighbors[(new_w, new_z, new_y, new_x)] += 1
                            except KeyError:
                                active_neighbors[(new_w, new_z, new_y, new_x)] = 1

    for coords in active_neighbors:
        active = False
        oob = False
        try:
            active = prev_pocket[coords[0]][coords[1]][coords[2]][coords[3]]
        except KeyError:
            oob = True

        if active and active_neighbors[coords] not in {2, 3}:
            if not oob:
                pocket_dim[coords[0]][coords[1]][coords[2]][coords[3]] = False
            else:
                if coords[0] not in pocket_dim:
                    pocket_dim[coords[0]] = {coords[1]: {coords[2]: {coords[3]: False}}}
                elif coords[1] not in pocket_dim[coords[0]]:
                    pocket_dim[coords[0]][coords[1]] = {coords[2]: {coords[3]: False}}
                elif coords[2] not in pocket_dim[coords[0]][coords[1]]:
                    pocket_dim[coords[0]][coords[1]][coords[2]] = {coords[3]: False}
                else:
                    pocket_dim[coords[0]][coords[1]][coords[2]][coords[3]] = False
        elif not active and active_neighbors[coords] == 3:
            if not oob:
                pocket_dim[coords[0]][coords[1]][coords[2]][coords[3]] = True
            else:
                if coords[0] not in pocket_dim:
                    pocket_dim[coords[0]] = {coords[1]: {coords[2]: {coords[3]: True}}}
                elif coords[1] not in pocket_dim[coords[0]]:
                    pocket_dim[coords[0]][coords[1]] = {coords[2]: {coords[3]: True}}
                elif coords[2] not in pocket_dim[coords[0]][coords[1]]:
                    pocket_dim[coords[0]][coords[1]][coords[2]] = {coords[3]: True}
                else:
                    pocket_dim[coords[0]][coords[1]][coords[2]][coords[3]] = True

    pretty_print(pocket_dim)
    # >>> 1816
