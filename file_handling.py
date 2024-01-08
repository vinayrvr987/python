s = "Entered this text into file using python"

with open("test.txt", "w") as f:
    f.write(s)

fp = open("test.txt", "w")
fp.write(s)
fp.close()

def print_from_file():
    with open("test.txt", "r") as f:
        print(f.read())

with open("test.txt", "a") as f:
    f.write(". This is what i am appending")

print_from_file()