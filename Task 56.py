Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> M=3
>>> arrs=[]
>>> for i in range(0,M):
	print("Enter string", end=' ')
	arrs.append(input())

	
Enter string 1010
Enter string 321
Enter string 2121
>>> for string in arrs
SyntaxError: invalid syntax
>>> for string in arrs:
	str_len = len(string)
	if str_len% !=0:
		
SyntaxError: invalid syntax
>>> printfor string in arrs:
	str_len = len(string)
	if (str_len%2) !=0:
		
SyntaxError: invalid syntax
>>> for string in arrs:
	str_len = len(string)
	if (str_len%2) !=0:
		print(string[math.cell(str_len/2)-1])

		
Traceback (most recent call last):
  File "<pyshell#14>", line 4, in <module>
    print(string[math.cell(str_len/2)-1])
AttributeError: module 'math' has no attribute 'cell'
>>> for string in arrs:
	str_len = len(string)
	if (str_len%2) !=0:
		print(string[math.ceil(str_len/2)-1])

		
2
>>> 
