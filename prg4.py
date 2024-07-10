import random
number = random.randint(1,10)
guess = 4
while guess != number:
    guess = int(input("Enter a Guess:"))
    if (guess > number):
        print("Number is higher than guess number")
    elif (guess < number):
        print("Number is lower than guess number")
    else:
        print("You Won!")