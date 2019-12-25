Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> N=4
>>> M=5
>>> L=2
>>> def get_row(column):
    col = []
    for i in range(0, column):
        col.append(random.randint(0, 99))
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
71 13 40 47 33 
3 84 17 93 20 
99 48 83 86 91 
65 36 70 51 19 
>>> max_element=False
>>> i=0
>>> while i< len(A):
	j=0
	while j< len(A[i]):
		if max_element is False or max_element < A[i][j]:
			max_element = A[i][j]
		j+=1
	i+=1

	
>>> i=0
>>> while i<len(A):
	j=0
	while j< len(A[i]):
		A[i][j]/=max_element
		A[i][j]=round(A[i][j],!)
		
SyntaxError: invalid syntax
>>> while i<len(A):
	j=0
	while j< len(A[i]):
		A[i][j]/=max_element
		A[i][j]=round(A[i][j],1)
		j+=1
	i+=1

	
>>> print("Max element:", max_element)
Max element: 99
>>> print_matrix(A)
0.7 0.1 0.4 0.5 0.3 
0.0 0.8 0.2 0.9 0.2 
1.0 0.5 0.8 0.9 0.9 
0.7 0.4 0.7 0.5 0.2 
>>> 
