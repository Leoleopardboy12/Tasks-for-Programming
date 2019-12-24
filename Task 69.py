Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> N = #row
SyntaxError: invalid syntax
>>> N = 2 #row
>>> M= 3 #column
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

>>> def listsum(list):
	sum = 0
	for element in list:
		sum += elementreturn sum
		
SyntaxError: invalid syntax
>>> def listsum(list):
	sum = 0
	for element in list:
		sum += element return sum
		
SyntaxError: invalid syntax
>>> def listsum(list):
	sum = 0
	for element in list:
		sum += element
	return sum

>>> def print_matrix(matrix):
	i=0
	while i < len(matrix):
		j=0
		row = matrix[i]
		while j<len(row):
			column = row[j]
			print(column, end=' ')
			j+=1
		print()
		i+=1

		
>>> A= get_matrix(N,M)
>>> tmp=list(zip(*))
SyntaxError: invalid syntax
>>> tmp=list(zip(*A))
>>> sum_max = 0
>>> index_column_sum = 0
>>> i=0
>>> while i<len(tmp):
	column = tmp[i]
	current_list_sum = listsum(column)
	if current_list_sum >sum_max:
		index_column_sum =1
		sum_max = current_list_sum
	i+=1

	
>>> print_matrix(A)
7 5 2 
0 8 0 
>>> print(i)
3
>>> 
