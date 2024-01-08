# lists are mutable
list_of_idiots = [["1", "Vinay"], ["2", "Kushal"]]
print(f"List is {list_of_idiots}")

l1 = [12, 34, 542, 246]
print(l1)
l1.remove(12)
print(l1)
l1.sort()
print(l1)
l1.pop()
print(l1)
l1.append(89)
print(l1)
l1.clear()
print(l1)
l1.extend([32, 798, 78])
print(l1)
print(l1.index(32))

# tuples are immutable
tuple_1 = ("vinay", "pooja", "rbk", "manjula")
print(tuple_1)

t = (113, 54, 53, 53)
print(t)

print(t.count(54))
print(t.index(53))

# sets - Not having any duplicate values
init_set = set()  # to initialize set
set_of_vegs = {"carrot", "beans"}
print(set_of_vegs)
set_of_vegs.add("potato")
print(set_of_vegs)
set_of_vegs.remove("carrot")
print(set_of_vegs)
par_veg = set_of_vegs.pop()
print(set_of_vegs)
dummy_num_set = {1, 2, 3}
union = dummy_num_set.union(set_of_vegs)  # union, intersection, differance
print(union)

print(2 in dummy_num_set)
print(2 in set_of_vegs)
print("v" in "vinay")

#Dictionaries
dict1 = {}
print(dict1, type(dict1))

marks = {"kushal": 0, "vinay": 100, "pooja": 99}
print(marks["kushal"])
print(marks.get("kushal"))
# print(marks["gandu"]) -> Throw Error
print(marks.get("gandu"))
print(marks.keys())
print(marks.values())
print(marks.items())
