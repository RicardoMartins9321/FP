"""Print the name and representation (repr) of an object,
followed by the name and representation of each of its elements,
if the object is a list, tuple or dict.
"""

"""
This function checks the type of the input object, and if it is a list, tuple or dictionary, 
it prints the object and also recursively calls the explodeObject function for each element
of the object. The recursion is used to continue the process for each nested element and 
also ensures that all the output is printed as strings."""

def explodeObject(name, obj):   
   if type(obj) in [int, float]:
      print(name + " = " + str(obj))
   elif type(obj) == str:
      print(name + " = " + "'" + str(obj) + "'")
   elif type(obj) == list:
      print(name + " = " + str(obj))
      for i in range(len(obj)):
         explodeObject(name + "[" + str(i) + "]", obj[i])
   elif type(obj) == tuple:
      print(name + " = " + str(obj))
      for i in range(len(obj)):
         explodeObject(name + "[" + str(i) + "]", obj[i])
   elif type(obj) == dict:
      print(name + " = " + str(obj))
      for key in obj:
         explodeObject(name + "[" + "'" + str(key) + "'" + "]", obj[key])

def main():
   obj1 = [1, ["a", ["b", 2], 3], 4]
   obj2 = [1, "ola", (2, [[3, 4], 5, ("adeus", 6)], 7)]
   obj3 = [1, {"ola": "hello", "adeus": ["bye", "adieu"]}, (2, [[3, 4], 5], 6)]
   
   print(explodeObject("obj1", obj1))
   print(explodeObject("obj2", obj2))
   print(explodeObject("obj3", obj3))


if __name__ == "__main__":
   main()



   