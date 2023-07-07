"""
If the input string is empty, the function returns an empty string.

This function takes in a string S and using recursion, it checks if the first character of S is an uppercase letter. 
If it is, it adds that character to the result string and recursively calls the function for the remaining characters. 
If it's not an uppercase letter, it skips that character and calls the function for the remaining characters.

It uses isupper() method from string class to check if the current character is uppercase or not."""

def onlyCaps(S):
    if not S:
        return ""
    if S[0].isupper():
        return S[0] + onlyCaps(S[1:])
    else:
        return onlyCaps(S[1:])
