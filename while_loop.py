# Number guessing game
number = 7


while True:
    user_input = input("Would you like to play? (Y/N)").lower()
    if user_input == 'n':
        print("Bye!")
        break
    user_input = int(input("Guess the number: "))
    if user_input == number:
        print(f"Yay {number} is correct")
    elif user_input > number:
        print(f"Number you've entered is incorrect and greater")
    else:
        print(f"Number {user_input} is less")
