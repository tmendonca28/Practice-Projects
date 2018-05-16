import types

favorite_things = ["anthony", "george", "mendonca"]
# can use += to add a single item to the list
# favorite_things += ["jackie"]
# favorite_things.append("item")
# del favorite_things[-1] removes last item from list
# favorite_things.extend(list) extends list with items from another list
# favorite_things.insert(index, value)

messy_list = ["a", 2, 3, 1, False, [1, 2, 3]]

# Pop value at index 3 and add it to the beginning of messy_list
#messy_list.insert(0, messy_list.pop(3))

# remove all other values except integers
messy_list = [x for x in messy_list if type(x) == int]
print(messy_list)
