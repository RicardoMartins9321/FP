"""
This function takes in a string s, and using recursion, it checks if the first character of s is an "x". 
If it is, it recursively calls the function for the remaining characters and adds the "x" to the end 
of the resulting string. If the first character is not "x", it adds the character to the resulting 
string and recursively calls the function for the remaining characters.

If the input string is empty, the function returns an empty string."""

def endX(s):
    if not s:
        return ""
    if s[0] == "x":
        return endX(s[1:]) + "x"
    else:
        return s[0] + endX(s[1:])

print(endX("xxre")) # => "rexx"
print(endX("xxhixx")) # => "hixxxx"
print(endX("hixhix")) # => "hihixx"
