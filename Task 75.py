Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> N=5
>>> M=7
>>> L=3
>>> K=2
>>> def get_row(column):
    col = []
    for i in range(0, column):
        col.append(random.randint(-9, 9))
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
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    A=get_matrix(N,M)
  File "<pyshell#7>", line 4, in get_matrix
    matrix.append(get_row(column))
  File "<pyshell#5>", line 4, in get_row
    col.append(random.randint(-9, 9))
NameError: name 'random' is not defined
>>> 
================================ RESTART: Shell ================================
>>> import random
>>> N=5
>>> M=7
>>> L=3
>>> K=2
>>> def get_row(column):
    col = []
    for i in range(0, column):
        col.append(random.randint(-9, 9))
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
>>> print_matrix
<function print_matrix at 0x00000230E21D90D0>
>>> print_matrix(A)
2 2 8 -2 -4 4 -8 
-6 -3 6 9 -6 8 8 
5 -3 -3 5 -6 4 -2 
9 -5 -5 -8 -7 8 4 
-5 7 8 -3 -1 9 0 
>>> L_zeros = 0
>>> 
>>> K_zeros=0
>>> i=0
>>> while i < len(A):
    j = 0
    while j < len(A[i]):
        if A[i][j] == 0:
            if i < L:
		    l_zeros += 1
		    
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> while i < len(A):
	j=0
	while j<len(A[i]):
		if A[i][j] == 0:
			if i < L:
				L_zeros+=1
			if j < K:
				K_zeros+=1
		j+=1
	i+=1

	
>>> print(L, L_zeros)
3 0
>>> print(K,K_zeros)
2 0
>>> 
