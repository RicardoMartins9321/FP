"""
The function uses two nested for loops to calculate the sum of cubes of all possible pairs of numbers 
whose value is less than R. It stores the results in a dictionary, where the keys are the sum of cubes 
and the values are lists of tuples representing the pairs of numbers that resulted in that sum.

Finally, the function loops through the dictionary and prints the results for all 
numbers that have more than one pair of numbers that resulted in their cube sum.
"""
def cubes(R):
    cubes_dict = {}
    for i in range(1, R):
        for j in range(i+1, R):
            sum_of_cubes = i**3 + j**3
            if sum_of_cubes in cubes_dict:
                cubes_dict[sum_of_cubes].append((i, j))
            else:
                cubes_dict[sum_of_cubes] = [(i, j)]
                
    # print(cubes_dict) - the dictionary contains all the different combinations
    # but only the ones which appeared more than once have a len > 1, therefore
    # only the numbers with diferent combinations will be shown
    for key, value in cubes_dict.items():
        if len(value) > 1:
            print(f"{key}: {value}")

print(cubes(20))
print(cubes(50))
