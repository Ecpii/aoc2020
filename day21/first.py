import copy

# this code might be one of my worst solutions yet
with open("input.txt") as inp:
    raw_nutritional_info = inp.read().split('\n')[:-1]

possible_allergen_map = {}
possible_allergen_ingredients = set()
all_ingredients = set()
determined_ingredients = set()
determined_pairs = {}

for item_nutritional_info in raw_nutritional_info:
    allergens = item_nutritional_info[item_nutritional_info.index('(') + 10:-1]
    ingredients = set(item_nutritional_info[:item_nutritional_info.index('(') - 1].split(' '))
    all_ingredients |= ingredients
    if ', ' in allergens:
        allergens = allergens.split(', ')
    else:
        allergens = [allergens]

    for allergen in allergens:
        if allergen in possible_allergen_map:
            possible_allergen_map[allergen] &= ingredients
        else:
            possible_allergen_map[allergen] = ingredients.copy()

for allergen in possible_allergen_map:
    possible_allergen_ingredients |= possible_allergen_map[allergen]

previous_allergen_map = {}
while previous_allergen_map != possible_allergen_map:
    previous_allergen_map = copy.deepcopy(possible_allergen_map)
    for allergen in possible_allergen_map:
        if len(possible_allergen_map[allergen]) == 1:
            sole_ingredient, = possible_allergen_map[allergen]
            determined_pairs[sole_ingredient] = allergen
            determined_ingredients.add(sole_ingredient)
            continue
        shared_ingredients = possible_allergen_map[allergen] & determined_ingredients
        if shared_ingredients:
            for shared_ingredient in shared_ingredients:
                possible_allergen_map[allergen].discard(shared_ingredient)

allergen_ingredient_sum = 0
safe_ingredients = all_ingredients - possible_allergen_ingredients
for item_nutritional_info in raw_nutritional_info:
    ingredients = item_nutritional_info[:item_nutritional_info.index('(') - 1].split(' ')
    for ingredient in ingredients:
        if ingredient in safe_ingredients:
            allergen_ingredient_sum += 1

print(allergen_ingredient_sum)
# >>> 2307
