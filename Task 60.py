Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
M
>>> M=3
>>> list_strings=[]
>>> for i in range(0,M)
SyntaxError: invalid syntax
>>> for i in range(0,M):
	print("line", end='')
	list_strings.append(input())

	
line

line
line
>>> 
>>> 
>>> for string in list_strings:
	string = re.sub(r'\?', '*', string)
	print(string)

	



>>> 
>>> print(list_strings)
['', '', '']
>>> # -*- coding:utf-8 -*-
>>> 
>>> print(list_strings)
['', '', '']
>>> 
================================ RESTART: Shell ================================
>>> import re
>>> M=3
>>> list_strings=[]
>>> for i in range(0,M):
	print("Enter string", end=' ')
	list_string.append(input())

	
Enter string Traceback (most recent call last):
  File "<pyshell#26>", line 3, in <module>
    list_string.append(input())
NameError: name 'list_string' is not defined
>>> for i in range(0,M):
	print("Enter string", end=' ')
	list_strings.append(input())

	
Enter string Hello
Enter string Hello?
Enter string Yes
>>> for string in list_strings:
	string = re.sub(r'\?', '*', string)
	print(string)

	
Hello
Hello*
Yes
>>> 
