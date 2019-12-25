Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> M=2
>>> arrs=[]
>>> for i in range(0,M):
	print("Enter string", end=' ')
	arrs.append(input())

	
Enter string Salutations
Enter string Goodbye
>>> max_str_len=0
>>> for str in arrs:
	str_len =len(str)

	
>>> if str_len>max_str_len:
	max_str_len = str_len

	
>>> print("Longest string", max_str_len)
Longest string 7
>>> for str in arrs:
	str_len = len(str)

	
>>> if str_len<max_str_len:
	for i in range(0,max_str_len - str_len):
		str= '*' +str

		
>>> print(str)
Goodbye
>>> 
