name = input("Enter name to see greatness: ").lower()

if name == "vinay":
    print("great")
elif name == "kushal":
    print("dumb")
else:
    print("not great")

movies_watched = {"oppenheimer", "barbie"}
user_input = input("Enter name of a movie")

print(user_input in movies_watched)

if user_input in movies_watched:
    print(f"watched this movie thanks")
else:
    print(f"Not watched. go away")
