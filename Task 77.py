Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> N+4
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    N+4
NameError: name 'N' is not defined
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

>>> ef print_matrix(matrix):
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
        
SyntaxError: invalid syntax
>>> 
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
8 8 4 8 1 
2 0 7 0 7 
9 7 1 3 2 
8 9 5 1 3 
>>> L_row = A[L-1].copy()
>>> i=0
>>> while i<len(A):
	j=0
	while j< len(A[i]):
		A[i][j] += l_row[j]
		j+=1
	i+=1

	
Traceback (most recent call last):
  File "<pyshell#28>", line 4, in <module>
    A[i][j] += l_row[j]
NameError: name 'l_row' is not defined
>>> while i<len(A):
	j=0
	while j< len(A[i]):
		A[i][j] += L_row[j]
		j+=1
	i+=1

	
>>> print_matrix(A)
10 8 11 8 8 
4 0 14 0 14 
11 7 8 3 9 
10 9 12 1 10 
>>> 
