try:
    number = int(input("Enter a number: "))
    print(number)
except Exception as e:
    print("Some error occured: ", e)