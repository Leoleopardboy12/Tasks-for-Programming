Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from datetime import datetime
>>> M= 3
>>> arrs=[]
>>> for i in range(0,M):
	print("Enter string", end=' ')
	arrs.append(input())

	
Enter string 11
Enter string 12
Enter string 5
>>> now =str(datetime.now())
>>> for string in arrs:
	print(string.replace('.','.' +now))

	
11
12
5
>>> print(now)
2019-12-25 20:13:40.294888
>>> 
