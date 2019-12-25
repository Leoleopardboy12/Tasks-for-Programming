Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> N=4
>>> M=5
>>> K=2
>>> def get_row(column):
    col = []
    for i in range(0, column):
        col.append(random.randint(0, 9))
    return col

>>> def get_matrix(row, column):
    matrix = []
    for i in range(0, row):
        matrix.append(get_row(column))
    return matrix

>>> def print_matrix(matrix):
    i = 0
    while i < len(matrix):
        j = 0
        row = matrix[i]
        while j < len(row):
            column = row[j]
            print(column, end=' ')
            j += 1
        print()
        i += 1

        
>>> def get_column(matrix, index):
    column = []
    i = 0
    while i < len(matrix):
        column.append(matrix[i][index])
        i += 1
    return column

>>> a=get_matrix(N,M)
>>> A=get_matrix(N,M)
>>> print_matrix(A)
2 1 6 7 5 
0 3 2 7 0 
1 7 9 0 4 
3 3 9 4 4 
>>> K_column = get_column(A,K-1)
>>> i =0
>>> while i < len(A):
	j=0
	while j< len(A[i]):
		A[i][j]*=K_column[i]
		j+=1
	i+=1

	
>>> 
>>> print_matrix(A)
2 1 6 7 5 
0 9 6 21 0 
7 49 63 0 28 
9 9 27 12 12 
>>> 
