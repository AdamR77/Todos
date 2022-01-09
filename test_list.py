
example_list = [1, 2, 3, "ala ma kota", 5, 6, 7]
without_1stand_last = example_list[1:-1]
for element in without_1stand_last:
    example_list.remove(element)
#spr
print(without_1stand_last)
print(example_list)


