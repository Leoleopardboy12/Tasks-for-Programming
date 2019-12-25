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

        
>>> def get_column(matrix, index):
    column = []
    i = 0
    while i < len(matrix):
        column.append(matrix[i][index])
        i += 1
    return column

>>> A=get_matrix(N,M)
>>> print_matrix(A)
5 9 8 7 1 
3 4 0 9 7 
8 8 4 6 2 
8 3 9 2 3 
>>> og_matrix=A.copy()
>>> i=0
>>> while i <len(A)
SyntaxError: invalid syntax
>>> while i <len(A):
	j=0
	max_element=max(A[i])
	while j < len(A[i]):
		print(A[i][j], max(get_column(A,j)))
		A[i][j] /= max(get_column(og_matrix, i))
		A[i][j]=round(A[i][j], 1)
		j+=1
	i+=1

	
5 8
9 9
8 9
7 9
1 7
3 8
4 8
0 9
9 9
7 7
8 8
8 8
4 9
6 6
2 3
8 8
3 3
9 9
2 2
3 3
>>> print_matrix(A)
0.6 1.1 1.0 0.9 0.1 
0.4 0.5 0.0 1.1 0.9 
0.9 0.9 0.4 0.7 0.2 
4.0 1.5 4.5 1.0 2.7 
>>> 
