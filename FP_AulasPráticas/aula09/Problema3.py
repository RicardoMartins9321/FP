def mediana(lst):
    #return sum(lst) / len(lst)

    lst.sort()
    
    half = len(lst)//2 - 1

    if len(lst) % 2 == 0:
        return (lst[half] + lst[half+1]) / 2
    else:
        return lst[half+1]

def median(numbers):
    # Sort the list in ascending order
    numbers.sort()

    # Find the length of the list
    length = len(numbers)

    # If the length of the list is odd, return the middle element
    if length % 2 != 0:
        return numbers[length // 2]
    # If the length of the list is even, return the average of the two middle elements
    else:
        middle1 = numbers[length // 2 - 1]
        middle2 = numbers[length // 2]
        return (middle1 + middle2) / 2

def main():
    lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lst2 = [4, 3, 8, 3, 5]
    lst3 = [1, 2, 12, 7, 5, 2, 8, 3, 9, 5]

    print(mediana(lst1))
    print(mediana(lst3))
    print(median(lst2))

if __name__ == "__main__":
    main()