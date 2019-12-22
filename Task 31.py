Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def bubbleSort(arr)
SyntaxError: invalid syntax
>>> def bubbleSort(arr)
SyntaxError: invalid syntax
>>> arr= [1,2,3,4,5,44,221,76,333,9]
>>> def bubbleSort(arr)
SyntaxError: invalid syntax
>>> def bubbleSort(arr):
	n = len(arr)
	for i in range(n):
		for j in range(0, n-i-1):
			if arr[j]>arr[j+1]:
				arr[j],arr[j+1] =arr[j+1], arr[j]

				
>>> for i in range(len(arr)):
	print(%arr[i])
	
SyntaxError: invalid syntax
>>> for i in range(len(arr)):
	print(% arr[i])
	
SyntaxError: invalid syntax
>>> for i in range(len(arr)):
	print("%d" %arr[i])

	
1
2
3
4
5
44
221
76
333
9
>>> def bubbleSort(arr):
	n = len(arr)
	for i in range(n):
		for j in range(0, n-i-1):
			if arr[j]>arr[j+1]:
				arr[j],arr[j+1] =arr[j+1], arr[j]
				else:
					
SyntaxError: invalid syntax
>>> 
>>> def bubbleSort(arr):
	n = len(arr)
	for i in range(n):
		for j in range(0, n-i-1):
			if arr[j]>arr[j+1]:
				arr[j],arr[j+1] =arr[j+1], arr[j]
			else:
				a=o

>>> for i in range(len(arr)):
	print("%d" %arr[i])

	
1
2
3
4
5
44
221
76
333
9
>>> for i in range(len(arr)):
	print(arr)

	
[1, 2, 3, 4, 5, 44, 221, 76, 333, 9]
[1, 2, 3, 4, 5, 44, 221, 76, 333, 9]
[1, 2, 3, 4, 5, 44, 221, 76, 333, 9]
[1, 2, 3, 4, 5, 44, 221, 76, 333, 9]
[1, 2, 3, 4, 5, 44, 221, 76, 333, 9]
[1, 2, 3, 4, 5, 44, 221, 76, 333, 9]
[1, 2, 3, 4, 5, 44, 221, 76, 333, 9]
[1, 2, 3, 4, 5, 44, 221, 76, 333, 9]
[1, 2, 3, 4, 5, 44, 221, 76, 333, 9]
[1, 2, 3, 4, 5, 44, 221, 76, 333, 9]
>>> 
================================ RESTART: Shell ================================
>>> def bubbleSort(arrs):
	n = len(arrs)
	for i in range(n):
		for j in range(0, n-i-1):
			if arrs[j]>arrs[j+1]:
				arr[j],arrs[j+1] =arrs[j+1], arrs[j]

				
>>> arrs = [1,2,3,4,5,44,221,76,333,9]
>>> bubbleSort(arrs)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    bubbleSort(arrs)
  File "<pyshell#32>", line 6, in bubbleSort
    arr[j],arrs[j+1] =arrs[j+1], arrs[j]
NameError: name 'arr' is not defined
>>> def bubbleSort(arrs):
	n = len(arrs)
	for i in range(n):
		for j in range(0, n-i-1):
			if arrs[j]>arrs[j+1]:
				arrs[j],arrs[j+1] =arrs[j+1], arrs[j]

				
>>> arrs = [1,2,3,4,5,44,221,76,333,9]
>>> bubbleSort(arrs)
>>> for i in range(len(arrs)):
	print("%d" %arrs[1])

	
2
2
2
2
2
2
2
2
2
2
>>> for i in range(len(arrs)):
	print("%d" %arrs[i])

	
1
2
3
4
5
9
44
76
221
333
>>> 
