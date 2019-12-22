Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> arrs = [1,2,3,4,5,6,7,8,11,22,333,54,67]
>>> K=4
>>> arrs2 = [77,44,88,9,10]
>>> for arrs[K]:
	
SyntaxError: invalid syntax
>>> arrs.insert(K, arrs2)
>>> pirnt(arrs)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    pirnt(arrs)
NameError: name 'pirnt' is not defined
>>> print(arrs)
[1, 2, 3, 4, [77, 44, 88, 9, 10], 5, 6, 7, 8, 11, 22, 333, 54, 67]
>>> arrs = [1,2,35,6,7,8,9]
>>> K=4
>>> arrs2= [3,4,5]
>>> 
>>> for i in range(len(arrs2)):
	arrs.insert(i+K, arrs2[i])

	
>>> print(arrs)
[1, 2, 35, 6, 3, 4, 5, 7, 8, 9]
>>> 
