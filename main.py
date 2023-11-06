from random import randint

random_number = randint(1, 10)
guess = None

while guess != random_number:
    guess = input('Guess a number from 1 - 10 : ')
    guess = int(guess)
if guess < random_number:
    print("YOUR NUMBER IS  TOO LOW")
elif guess > random_number:
    print("YOUR NUMBER IS TOO BIG")
else:
    print("YOU WIN!!")
