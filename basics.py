# numbers
float_division = 3 / 2
integer_division = 3 // 2  # if you want to remove decimal part
print(float_division)
print(integer_division)

remainder = 36 % 2
print(remainder)

# strings and formatting
NAME = "Vinay"
sample_string = "hey! that is a big \"FAECT\""
print(sample_string + str(20))

print(f"hey it is {sample_string}")

# formatting
template = "hey it is {}"
print(template.format(NAME))

template2 = "hey it is {name}"
print(template2.format(name=NAME))

multiline_string = """ Hey! This is vinay
who is living in chennai, india.
"""
print(multiline_string)

# User Input
age = int(input("Age please:") or "23")
print(f"your age is {age * 12}, in months")

# Boolean operators
form_16 = "yes"
eligible_for_loan = age > 18 and form_16 == "yes"
print(f"Are you eligible for loan? Ans: {eligible_for_loan}")
