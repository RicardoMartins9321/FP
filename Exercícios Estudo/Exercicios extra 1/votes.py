"""
This function takes in two arguments, "votes" which is a list of integers representing the number 
of votes for each party and "numseats" which is an integer representing the number of seats available.

It initializes a variable "seats" as a list of zeroes with the same length as "votes". 
It then enters a for loop starting at 0 and ending at "numseats". 
In each iteration, it calculates quotients by dividing the votes by the number of seats already assigned +1 for each party. 
Then it finds the indexes of the parties that have the maximum quotient using a list comprehension. 
Then it finds the index of the party with the minimum vote among those parties using the min() function 
with the key argument that uses the getitem method of the votes list. It increments the value of the corresponding 
index in the "seats" list by 1. Once the loop completes, it returns the "seats" list which represents the distribution 
of deputies for each party. This way, if there are two parties with a maximum Q, the seat is assigned to the least voted party."""

def hondt(votes, numseats):
    seats = [0] * len(votes)    # multiplying by [0] creates a list with the choosen size
    #print(seats)
    for _ in range(numseats):
        quotients = [v / (s+1) for v,s in zip(votes, seats)]
        print(tuple(zip(votes, seats)))
        #print(quotients)
        max_quotient = max(quotients)
        max_indexes = [i for i, quotient in enumerate(quotients) if quotient == max_quotient]
        min_vote_index = min(max_indexes, key=votes.__getitem__)
        seats[min_vote_index] += 1

    return seats

print("[7000, 12000, 6000, 5000], 5 =>",hondt([7000, 12000, 6000, 5000], 5))  # => [1, 2, 1, 1]
print("[15300, 12000, 6600, 5100], 6 =>", hondt([15300, 12000, 6600, 5100], 6))  # => [2, 2, 1, 1]