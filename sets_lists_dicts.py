# lists are mutable
list_of_idiots = [["1", "Vinay"], ["2", "Kushal"]]
print(f"List is {list_of_idiots}")

#tuples are immutable
tuple_1 = ("vinay", "pooja", "rbk", "manjula")
print(tuple_1)

#sets - Not having any duplicate values
init_set = set() #to initialize set
set_of_vegs = {"carrot", "beans"}
print(set_of_vegs)
set_of_vegs.add("potato")
print(set_of_vegs)
set_of_vegs.remove("carrot")
print(set_of_vegs)
par_veg = set_of_vegs.pop()
print(set_of_vegs)
dummy_num_set = {1,2,3}
union = dummy_num_set.union(set_of_vegs) #union, intersection, differance
print(union)

print(2 in dummy_num_set)
print(2 in set_of_vegs)
print("v" in "vinay")
