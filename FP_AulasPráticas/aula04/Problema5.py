import random


def hilo():
    number = random.randrange(1, 100)
    print(number)
    n = int(input('Take a guess: '))
    guess = 0
    if n == number:
        print(f'You got it! Took you {guess} guesses!')
    elif n != number:
        if n != number:
            if n > number:
                guess += 1
                print('Lower')
            else:
                guess += 1
                print('Higher')
    while n != number:
        n = int(input('Take a guess: '))
        if n == number:
            guess += 1
            print(f'You got it! Took you {guess} guesses!')
        if n != number:
            if n > number:
                guess += 1
                print('Lower')
            else:
                guess += 1
                print('Higher')
    return guess


hilo()
