import random
number=random.randrange(1,9)
value = random.random(number)
guess =int(input("guess a number between 1 and 9"))
while chance < 5:
    if guess == value:
        print("you win")
if not chance < 5:
    print("you lose the number is"+ value)
