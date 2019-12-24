Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> N = 2
>>> M=3
>>> def get_row(column):
	col = []
	for i in range(0, column):
		col.append(random.randint(0, 9))
	return col

>>> 
>>> def get_matrix(row, column):
	matrix = []
	for i in range(0, row):
		matrix.append(get_row(column))
	return matrix

>>> def print_matrix(matrix):
	i=0
	while i< len(matrix):
		j=0
		row =matrix[i]
		while j< len(row):
			column = row[j]
			print(column, end=' ')
			j+=1
		print()
		i+=1

		
>>> def get_average(row):
	sum = 0
	for element in row:
		sum+=element
	return sum/len(row)

>>> A =get_matrix(N,M)
>>> print_matrix(A)
8 7 1 
4 0 5 
>>> n = 0
>>> for row in A:
	average = get_average(row)
	if average >n:
		n=average

		
>>> print(n)
5.333333333333333
>>> 
