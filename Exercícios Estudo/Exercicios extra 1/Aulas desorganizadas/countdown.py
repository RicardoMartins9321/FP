import time

# Function that makes a countdown of a given number
def countdown(N):
    while N > 0:
        time.sleep(1.0)
        N -= 1
        print(N)


N = int(input('Enter a number: '))

print(N)
countdown(N)

