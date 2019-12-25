Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> M=3
>>> list_strings=[]
>>> for i in range(0,M);
SyntaxError: invalid syntax
>>> for i in range(0,M):
	print("Enter string", end=' ')
	list_strings.append(input())

	
Enter string Hello
Enter string String
Enter string Perfection
>>> for string in list_strings:
	count_spaces=len(re.findall(r'\s', string))
	print(string,count_spaces)

	
Hello 0
String 0
Perfection 0
>>> list_strings.append("He LLo")
>>> print(string, count_spaces)
Perfection 0
>>>  for string in list_strings:
	count_spaces=len(re.findall(r'\s', string))
	print(string,count_spaces)
	
SyntaxError: unexpected indent
>>> for string in list_strings:
	count_spaces=len(re.findall(r'\s', string))
	print(string,count_spaces)

	
Hello 0
String 0
Perfection 0
He LLo 1
>>> 
