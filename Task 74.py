Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> N=4
>>> M=5
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
>>> print_matrix(A)
-8 5 -5 9 1 
9 -1 -3 5 -9 
-2 9 0 4 -5 
4 -2 -7 7 9 
>>> new_row=[]
>>> i=0
>>> while i < len(A):
    j = 0
    count_row_negative = 0
    while j < len(A[i]):
        is_negative = A[i][j] < 0
        if is_negative:
            count_row_negative += 1
        if len(new_row) <= j:
            new_row.append(1 if is_negative else 0)
        else:
		new_row[j] += 1 if is_negative else 0
		
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> while i < len(A):
    j = 0
    count_row_negative = 0
    while j < len(A[i]):
        is_negative = A[i][j] < 0
        if is_negative:
            count_row_negative += 1
        if len(new_row) <= j:
            new_row.append(1 if is_negative else 0)
        else:
		new_row[j] += 1 if is_negative else 0
		
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> while i < len(A):
    j = 0
    count_row_negative = 0
    while j < len(A[i]):
        is_negative = A[i][j] < 0
        if is_negative:
            count_row_negative += 1
        if len(new_row) <= j:
		new_row.append(1 if is_negative else 0)
		
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> while i < len(A):
	j=0
	count_row_negative = 0
	while j < len(A[i]):
		is_negative = A[i][j] < 0
		if is_negative:
			count_row_negative += 1
		if len(new_row) <= j:
			new_row.append(1 if is_negative else 0)
		else:
			new_row[j] += 1 if is_negative else 0
		j+=1

		
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    while i < len(A):
KeyboardInterrupt
>>> while i < len(A):
	j=0
	count_row_negative = 0
	while j < len(A[i]):
		is_negative = A[i][j] < 0
		if is_negative:
			count_row_negative += 1
		if len(new_row) <= j:
			new_row.append(1 if is_negative else 0)
		else:
			new_row[j] += 1 if is_negative else 0
		j+=1
	 A[i].append(count_row_negative)
	 
SyntaxError: unindent does not match any outer indentation level
>>> while i < len(A):
	j=0
	count_row_negative = 0
	while j < len(A[i]):
		is_negative = A[i][j] < 0
		if is_negative:
			count_row_negative += 1
		if len(new_row) <= j:
			new_row.append(1 if is_negative else 0)
		else:
			new_row[j] += 1 if is_negative else 0
		j+=1
	A[i].append(count_row_negative)
	i+=1

	
>>> A.append(new_row)
>>> print_matrix(A)
-8 5 -5 9 1 2 
9 -1 -3 5 -9 3 
-2 9 0 4 -5 2 
4 -2 -7 7 9 2 
1046980 2 1046981 0 2 
>>> 
