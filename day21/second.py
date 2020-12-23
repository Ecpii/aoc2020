from first import determined_pairs

allergen_ingredient_pairs = {
    determined_pairs[ingredient]: ingredient
    for ingredient in determined_pairs
}

alphabetized_allergens = [allergen for allergen in allergen_ingredient_pairs]
alphabetized_allergens.sort()

for allergen in alphabetized_allergens:
    print(allergen_ingredient_pairs[allergen], end=',')
# cljf,frtfg,vvfjj,qmrps,hvnkk,qnvx,cpxmpc,qsjszn, (remove trailing comma
