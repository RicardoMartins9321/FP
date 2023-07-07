"""
This function takes in a string called "inputStr" which is a 2 character input of a letter (a-h) and a number (1-8).
It assigns the first character in the string to the variable "column" and the second character (converted to integer) 
to the variable "row". Then, it checks if the column is in "aceg" and the row is odd or if the column is not in "aceg" and the row is even. 
If either of those conditions is true, it returns "Black", otherwise it returns "White".
"""

inputStr = input("Choose a position on the board: ")

def chess_square_color(inputStr):
 column, row = inputStr[0], int(inputStr[1])
 if (column in "aceg") == (row % 2 == 1):
     return "Black"
 return "White"

print(chess_square_color(inputStr))


if (inputStr[0] in ["a","c","e","g"] and inputStr[1] in ["1","3","5","7"]) or (inputStr[0] in ["b","d","f","h"] and inputStr[1] in ["2","4","6","8"]):
   print("Black")
elif (inputStr[0] in ["a","c","e","g"] and inputStr[1] in ["2","4","6","8"]) or (inputStr[0] in ["b","d","f","h"] and inputStr[1] in ["1","3","5","7"]):
   print("White")
else:
    print("That position is invalid!")