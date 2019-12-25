Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> N=4
>>> M=5
>>> L=2
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

        
>>> A=get_matrix(N,M)
>>> print_matrix(A)
2 7 1 5 5 
7 6 5 9 9 
8 2 8 7 2 
1 1 4 2 8 
>>> i=0
>>> while i < len(A):
	j=0
	max_element=max(A[i])
	while j < len(A[i]):
		A[i][j]/=max_element
		A[i][j] = round(A[i][j], 1)
		j+=1
	i+=1

	
>>> print_matrix(A)
0.3 1.0 0.1 0.7 0.7 
0.8 0.7 0.6 1.0 1.0 
1.0 0.2 1.0 0.9 0.2 
0.1 0.1 0.5 0.2 1.0 
>>> 
