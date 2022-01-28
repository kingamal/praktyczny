from random import randint

answer = randint(1, 20)

guess_as_str = input("Guess the number: ")
guess = int(guess_as_str)
while guess != answer :
    if guess < answer :
        print("To small!")
    else:
        print("Too big!")
    guess_as_str = input("Guess the number: ")
    guess = int(guess_as_str)

print("Bravo!")
