Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def bubbleSort(arrs):
	n = len(arrs)
	for i in range(n):
		for j in range(0, n-i-1)"
		
SyntaxError: EOL while scanning string literal
>>> def bubbleSort(arrs):
	n = len(arrs)
	for i in range(n):
		for j in range(0, n-i-1):
			arrs[:len(arrs)//2], arrs[len(arrs)//2:] = arrs[len(arrs)//2:], arrs[:len(arrs)//2]

			
>>> arrs = [1,2,3,4,5,6,7,8]
>>> bubbleSort(arrs)
>>> for i in range(len(arrs)):
	print(arrs[i])

	
1
2
3
4
5
6
7
8
>>> def bubbleSort(arrs):
	n = len(arrs)
	for i in range(n):
		for j in range(0, n-i-1):
			arrs[:len(arrs)//2] =A
			arrs[len(arrs)//2:]=B

			
>>> arrs = [1,2,3,4,5,6,7,8]
>>> bubbleSort(arrs)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    bubbleSort(arrs)
  File "<pyshell#14>", line 5, in bubbleSort
    arrs[:len(arrs)//2] =A
NameError: name 'A' is not defined
>>> def bubbleSort(arrs):
	n = len(arrs)
	for i in range(n):
		for j in range(0, n-i-1):
			def split_list(arrs):
				half = len(arrs)//2
				return arrs[half:], arrs[:half]

			
>>> arrs = [1,2,3,4,5,6,7,8]
>>> bubbleSort(arrs)
>>> split_list(arrs)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    split_list(arrs)
NameError: name 'split_list' is not defined
>>> print(arrs[i])
8
>>> 
>>> for i in range(len(arrs)):
	print(arrs[i])

	
1
2
3
4
5
6
7
8
>>> 
================================ RESTART: Shell ================================
>>> arrs = [1,2,3,4,5,6,7,8]
>>> A = arrs[:len(arrs)//2]
>>> B= arrs[len(arrs)//2:]
>>> print(arrs[B,A])
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print(arrs[B,A])
TypeError: list indices must be integers or slices, not tuple

>>> print(B,A)
[5, 6, 7, 8] [1, 2, 3, 4]
>>> 
================================ RESTART: Shell ================================
>>> def bubbleSort(arrs):
	n = len(arrs)
	for i in range(n):
		arrs[:len(arrs)//2], arrs[len(arrs)//2:] = arrs[len(arrs//2:], arrs[:len(arrs)//2]
								
SyntaxError: invalid syntax
>>> def bubbleSort(arrs):
	n = len(arrs)
	for i in range(n):
		arrs[:len(arrs)//2], arrs[len(arrs)//2:] = arrs[len(arrs)//2:], arrs[:len(arrs)//2]

		
>>> arrs =[1,2,3,4,5,6,7,8]
>>> bubbleSort(arrs)
>>> for i in range(len(arrs)):
	print(arrs[i])

	
1
2
3
4
5
6
7
8
>>> def bubbleSort(arrs):
	n = len(arrs)
	for i in range(n//2):
		arrs[:len(arrs)//2], arrs[len(arrs)//2:] = arrs[len(arrs)//2:], arrs[:len(arrs)//2]

		
>>> arrs =[1,2,3,4,5,6,7,8]
>>> bubbleSort(arrs)
>>> for i in range(len(arrs)):
	print(arrs[i])

	
1
2
3
4
5
6
7
8
>>> def bubbleSort(arrs):
	n = len(arrs)
	for i in range(n):
		arrs[:n//2], arrs[n//2:] = arrs[n//2:], arrs[:n//2]

		
>>> bubbleSort(arrs)
>>> for i in range(len(arrs)):
	print(arrs[i])

	
1
2
3
4
5
6
7
8
>>> arrs = [1,2,3,4,5,6,7,8]
>>> A = arrs[:len(arrs)//2]
>>> B= arrs[len(arrs)//2:]
>>> arrs = [B,A]
>>> for i in range(len(arrs)):
	print(arrs[i])

	
[5, 6, 7, 8]
[1, 2, 3, 4]
>>> arrs = [1,2,3,4,5,6,7,8]
>>> A = arrs[:len(arrs)//2]
>>> B= arrs[len(arrs)//2:]

>>> arrs = [B,A]
>>>  arrs = [B+A]
 
SyntaxError: unexpected indent
>>> arrs=[B+A]
>>> for i in range(len(arrs)):
	print(arrs[i])

	
[5, 6, 7, 8, 1, 2, 3, 4]
>>> 
