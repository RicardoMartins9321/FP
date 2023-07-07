# given a string s iterates over each element and sees if it exists inside of string t
# if it does change the given char to an underscore
def replaceCharactersWithUnderscores(s, t):
   for char in s:
      if char in t:
         s = s.replace(char, "_")
   return s


"""This function takes in two strings, "s" and "t". It uses a list comprehension to iterate through each character in "s", 
and for each character, if it occurs in "t", it replaces it with an underscore. Otherwise, it keeps the character. 
The list comprehension is then joined to form the final modified string and returned.
Please note that this function doesnot modify the original string s and create a new one."""
def replace_occurrences(s, t):
    return ''.join(['_' if c in t else c for c in s])


def main():
    s = input("Write the string s: ")
    t = input("Write the string t: ")
    print(replaceCharactersWithUnderscores(s, t))
    print(replace_occurrences(s, t))

if __name__ == "__main__":
    main()