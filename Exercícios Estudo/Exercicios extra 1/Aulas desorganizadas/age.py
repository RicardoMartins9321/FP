# A teenager is a person between 13 and 19 years old, inclusive.
# A child is under 13.  A grown-up is 20 or more.
# This program outputs the age category for a given input age.

age = int(input("Age? "))

if age < 13: cat = "child"

elif age > 20: cat = "grown-up"

elif 13 < age < 20: cat = "teenager"

else: 
    print("ERROR: invalid age!")
    exit(1)

print("Category:", cat)