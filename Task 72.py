Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> N=4
>>> M=6
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

        
>>> def get_average(row):
    sum = 0
    for element in row:
        sum += element
    return sum/len(row)

>>> def get_column(matrix, index):
    column = []
    i = 0
    while i < len(matrix):
        column.append(matrix[i][index])
        i += 1
    return column

>>> A=get_matrix(N,M)
>>> print_matrix(A)
4 1 1 6 5 5 
1 7 5 8 2 4 
9 5 0 2 7 5 
4 4 1 3 5 2 
>>> sum=0
>>> i=0
>>> while i < len(A):
	j=0

	
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    while i < len(A):
KeyboardInterrupt
>>> while i < len(A):
	j=0
	while j < len(A[i]):
		sum += A[i][j]
		j += 1
	i += 1

	
>>> i=0
>>> new_row=[]
>>> while i < len(A):
    j = 0
    while j < len(A[i]):
        if len(new_row) <= j:
            new_row.append(A[i][j])
        else:
            new_row[j] += A[i][j]
        j += 1
    i += 1

    
>>> i=0
>>> while i < len(new_row):
    new_row[i] = new_row[i]/sum
    i += 1

    
>>> A.append(new_row)
>>> print(sum)
96
>>> print_matrix(A)
4 1 1 6 5 5 
1 7 5 8 2 4 
9 5 0 2 7 5 
4 4 1 3 5 2 
0.1875 0.17708333333333334 0.07291666666666667 0.19791666666666666 0.19791666666666666 0.16666666666666666 
>>> 
