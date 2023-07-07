
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def main():
    print("Prime numbers")
    n = int(input("n? "))
    for i in range(2, n+1):
        if isPrime(i):
            print(i)

main()
