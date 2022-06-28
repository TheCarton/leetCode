import random

win = False
# TODO: Make the program not crash when the user inputs a non-integer,
# Make the program tell them whether they're too high or too low.
while not win:
    print("guessing game")
    guess = input("enter your guess \n")
    valid=False
    while not valid:
        try:
            guess = int(guess)
            valid = True
        except:
            guess = input("enter your guess \n")
    print("type of guess {}".format(type(guess)))
    print("{}".format(guess))
    answer = random.randint(2, 36)
    print("type of answer {}".format(type(answer)))
    win = answer == guess
    lose = not win
    if win:
        print("aw yay good job :)")
    if lose:
        print("aw you're a loser sorry :/")
