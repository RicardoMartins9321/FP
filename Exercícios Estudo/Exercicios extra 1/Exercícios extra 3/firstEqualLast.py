"""This function takes in a list called "lst" and initializes a variable "n" to 0. 
It then iterates through the list, starting at index 1 and ending at half the length of the list (to avoid unnecessary checks),
checking if the first "i" elements of the list are equal to the last "i" elements (with no overlapping). 
If they are, it updates the value of "n" to "i". 
Finally, it returns the value of "n" which represents the longest match."""

def firstEqualLast(lst):
   n = 0
   for i in range(1, len(lst)//2 + 1):
      if lst[:i] == lst[-i:]:
         n = i
   return n

def main():
    lst = input("Write a list, strings or numbers: ")
    print("Number of chars repeated:", firstEqualLast(lst))

if __name__ == "__main__":
    main()