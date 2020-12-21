with open('input.txt') as inp:
    raw_tiles = inp.read().split("\n\n")

raw_tiles[-1] = raw_tiles[-1][:-1]
tile_dict = {}

for raw_tile in raw_tiles:
    tile_id = int(raw_tile[raw_tile.index(' ') + 1:raw_tile.index(':')])
    tile_contents = raw_tile[raw_tile.index('\n') + 1:].split('\n')
    tile_dict[tile_id] = tile_contents

tile_edges = {}
for tile_id in tile_dict:
    current_tile = tile_dict[tile_id]
    current_tile_edge_list = [current_tile[0], '', current_tile[9], '']
    for row in current_tile:
        current_tile_edge_list[1] += row[0]
        current_tile_edge_list[3] += row[9]
    tile_edges[tile_id] = current_tile_edge_list

edge_matches = {
        tile_id:
        {
            i: set() for i in range(4)
        }
        for tile_id in tile_dict
    }

for tile_id in tile_dict:
    for i in range(len(tile_edges[tile_id])):
        tile_edge = tile_edges[tile_id][i]
        for other_tile_id in tile_edges:
            if other_tile_id == tile_id:
                continue
            if tile_edge in tile_edges[other_tile_id] or tile_edge[::-1] in tile_edges[other_tile_id]:
                edge_matches[tile_id][i].add(other_tile_id)

corner_id_product = 1
for tile_id in edge_matches:
    num_unmatched_edges = 0
    for edge_num in edge_matches[tile_id]:
        if not edge_matches[tile_id][edge_num]:
            num_unmatched_edges += 1
    if num_unmatched_edges == 2:
        corner_id_product *= tile_id

print(corner_id_product)
# >>> 14129524957217
