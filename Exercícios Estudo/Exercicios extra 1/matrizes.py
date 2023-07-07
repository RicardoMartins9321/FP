# By using the for in range you are ensuring that each of the new copies 
# has an unique ID, in contrast if you used * to create the copies they 
# would all share the same ID an be altered together
# https://stackoverflow.com/questions/10941032/why-cant-i-change-only-a-single-element-in-a-nested-list-in-python
# Devolve o número de linhas da matriz M.

"""
The first function matcols(M) returns the number of columns in matrix M by taking the length of the first row of the matrix.

The second function matzeros(m, n) creates a matrix of zeroes with m rows and n columns.
It uses nested list comprehension to create the matrix.

The third function matmult(A, B) calculates the matrix product AB by creating an empty matrix with the same 
number of rows as A and the same number of columns as B. 
Then it uses 3 nested loops to iterate through each element of the resulting matrix and calculate 
the dot product of the corresponding row of matrix A and column of matrix B."""

def matrows(M):
   return len(M)

def matcols(M):
   return len(M[0])

def matzeros(m, n):
   return [[0 for _ in range(n)] for _ in range(m)]

def matzerosTEST(m, n):
   M = [n * [0] for _ in range(m)] 
   M[0][1] = 1

   return M

def matmult(A, B):
   result = matzeros(len(A), len(B[0]))
   print(result)
   for i in range(len(A)):       # rows
      for j in range(len(B[0])): # columns
         for k in range(len(B)): # elements of each row for A; rows for B
            result[i][j] += A[i][k] * B[k][j]
            # print(result)
   return result

def matmultTEST(A, B):
   C = matmult(A, B)
   return A, B, C

def main():
   M = [[1, 2, 3], [4, 5, 6]]
   m = 3
   n = 4
   A = [[7, 8], [9, 0], [1, 2]]
   B = [[1, 2, 3], [4, 5, 6]]

   print(matcols(M))
   print()
   print(matzeros(m,n))
   print(matzerosTEST(m,n))
   print("")
   print(matmult(A, B))

if __name__ == "__main__":
   main()
