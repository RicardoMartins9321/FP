"""
This function takes in a dictionary "trains" which associates names of trains with their corresponding list of wagons. 
It initializes an empty dictionary "merchandise" which will be used to associate the names of trains that carry a specific merchandise.

The function uses a for loop to iterate over the items in the "trains" dictionary. 
For each train, it uses another for loop to iterate over the wagons in the train. 
For each wagon, it unpack the goods and the quantity and assign them to the goods and quantity variables.

It then checks if the goods is already present in the merchandise dictionary, if it is, 
it adds the name of the current train to the set of trains already associated with that goods. 
If the goods is not present in the merchandise dictionary, it creates a new key-value pair 
with the goods as the key and a set containing the name of the current train as the value.

Finally, the function returns the merchandise dictionary that associates 
the set of names of the trains that carry it to each type of merchandise."""
def trainsPerMerchandise(trains):
    merchandise = {}
    for name, train in trains.items():
        for wagon in train:
            goods, quantity = wagon
            if goods in merchandise:
                merchandise[goods].add(name)
            else:
                merchandise[goods] = set([name])
    return merchandise


"""
This function takes in a list "t" which represents the train, a string "m" which represents 
the type of goods and an integer "q" which represents the quantity of goods to be unloaded.

The function initializes a variable "i" with the value of the last index of the list "t". 
It then uses a while loop to iterate through the wagons in the train starting from the last one until 
it is able to unload the requested quantity of goods or until there are no more wagons in the train.

Inside the while loop, it checks if the type of goods in the current wagon is equal to the 
requested goods, and if it is, it checks if the quantity of goods in the current wagon is 
greater than the requested quantity. If it is, it subtracts the requested quantity from 
the current wagon and sets the q to zero to exit the while loop. If the quantity of goods 
in the current wagon is less than the requested quantity, it subtracts the quantity 
of goods in the current wagon from q and removes the current wagon from the train.

If it is able to unload the entire requested quantity, the function returns zero, 
otherwise it returns the remaining quantity of goods it was unable to unload."""
def unload(t, m, q):
    i = len(t)-1
    while q > 0 and i >= 0:
        if t[i][0] == m:
            if t[i][1] > q:
                t[i][1] -= q
                q = 0
            else:
                q -= t[i][1]
                t.pop(i)
        i -= 1
    return q

