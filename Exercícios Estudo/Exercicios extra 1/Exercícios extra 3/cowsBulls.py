import random

# generate a random number with 4 digits
answer = str(random.randint(1000, 9999))
print(answer)

# start the game
while True:
    guess = input("Guess a 4-digit number: ")
    cows = 0
    bulls = 0

    # check for correct digits in correct place (cows)
    for i in range(4):
        if guess[i] == answer[i]:
            cows += 1

    # check for correct digits in wrong place (bulls)
    for i in range(4):
        if guess[i] in answer:
            bulls += 1

    # subtract the number of cows from bulls to get the true number of bulls
    bulls -= cows

    if cows == 4:
        print("You win! The number was " + answer)
        break
    else:
        print(str(cows) + " cows, " + str(bulls) + " bulls")