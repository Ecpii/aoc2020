with open('testinput.txt') as inp:
    raw_tiles = inp.read().split("\n\n")

raw_tiles[-1] = raw_tiles[-1][:-1]
tile_dict = {}

for raw_tile in raw_tiles:
    tile_id = int(raw_tile[raw_tile.index(' ') + 1:raw_tile.index(':')])
    tile_contents = raw_tile[raw_tile.index('\n') + 1:].split('\n')
    tile_dict[tile_id] = tile_contents

tile_edges = {}


def find_edges(tile_id: int):
    current_tile = tile_dict[tile_id]
    current_tile_edge_list = [current_tile[0], '', current_tile[9], '']
    for row in current_tile:
        current_tile_edge_list[1] += row[0]
        current_tile_edge_list[3] += row[9]
    tile_edges[tile_id] = current_tile_edge_list


for tile_id in tile_dict:
    find_edges(tile_id)

edge_matches = {
        tile_id: [None for i in range(4)]
        for tile_id in tile_dict
    }

for tile_id in tile_dict:
    for edge_num in range(len(tile_edges[tile_id])):
        tile_edge = tile_edges[tile_id][edge_num]
        for other_tile_id in tile_edges:
            if other_tile_id == tile_id:
                continue
            if tile_edge in tile_edges[other_tile_id] or tile_edge[::-1] in tile_edges[other_tile_id]:
                edge_matches[tile_id][edge_num] = other_tile_id

corner_id_product = 1
for tile_id in edge_matches:
    if edge_matches[tile_id].count(None) == 2:
        corner_id_product *= tile_id

# print(corner_id_product)
# >>> 14129524957217
