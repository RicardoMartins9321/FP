import time


def countdown(N):
    while N > 0:
        time.sleep(0.5)
        N -= 1
        print(N)


N = int(input('Enter a number: '))

print(N)
countdown(N)
