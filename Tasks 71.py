Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> N=4
>>> M=5
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

>>> A = get_matrix(N, M)
>>> print_matrix(A)
3 8 0 9 7 
7 7 5 4 6 
7 6 5 9 0 
2 2 4 6 7 
>>> for row in A:
    average = get_average(row)
    row.append(average)

    
>>> i=0
>>> new_row=[]
>>> while i < len(A[0]):
    column = get_column(A, i)
    average = get_average(column)
    new_row.append(average)
    i += 1

    
>>> A.append(new_row)
>>> print_matrix(A)
3 8 0 9 7 5.4 
7 7 5 4 6 5.8 
7 6 5 9 0 5.4 
2 2 4 6 7 4.2 
4.75 5.75 3.5 7.0 5.0 5.2 
>>> 
