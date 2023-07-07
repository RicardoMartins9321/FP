"""
This function uses recursion to traverse through the object passed as an argument, and check for its type. 
If the object is a string, it appends it to a list. If it is a list, tuple or set, 
it iterates through the items, and recursively calls the function on each item. 
If the object is a dictionary, it iterates through the key, value pairs, 
and recursively calls the function on each key and value.

It uses isinstance() to check the type of obj and it's using recursion to traverse the object and get all the strings."""

def getAllStrings(obj):
    strings = []
    if isinstance(obj, str):
        strings.append(obj)
    elif isinstance(obj, (list, tuple, set)):
        for item in obj:
            strings.extend(getAllStrings(item))
    elif isinstance(obj, dict):
        for key, value in obj.items():
            strings.extend(getAllStrings(key))
            strings.extend(getAllStrings(value))
    return strings


def main():
   obj1 = ["one", 2, ["three", 4, [5, "six"]]]
   obj2 = [1, "a", ("b", [{"c", "d", 2}, 3, (4, "e")], "f")]
   obj3 = {"a": 1, "b": ["c", "d"], (2, ("x", 3)): obj1}
   print(getAllStrings(obj1))
   print(getAllStrings(obj2))
   print(getAllStrings(obj3))


if __name__ == "__main__":
   main()