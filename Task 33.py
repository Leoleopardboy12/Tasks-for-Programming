Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def bubbleSort(arrs):
	n= len(arrs)
	for i range(n):
		
SyntaxError: invalid syntax
>>> def bubbleSort(arrs):
	n= len(arrs)
	for i in range(n):
		for j in range(0, n-i-1):
			arrs[j], arrs[j+1] = arrs[j+1], arrs[j]

			
>>> arrs = [1,2,3,4,5,6,7,43]
>>> bubbleSort(arrs)
>>> for i in range(len(arrs));
SyntaxError: invalid syntax
>>> for i in range(len(arrs)):
	print(arrs[i])

	
43
7
6
5
4
3
2
1
>>> 
