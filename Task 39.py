Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> arrs = [random.randint(0,20) for iter in range(10)]
>>> print(arrs)
[17, 19, 16, 8, 17, 14, 16, 15, 11, 7]
>>> arrs.insert(5, None)
>>> print(arrs)
[17, 19, 16, 8, 17, None, 14, 16, 15, 11, 7]
>>> for i in range(len(arrs)):
	if arrs[i] ==None:
		del arrs[i]

		
Traceback (most recent call last):
  File "<pyshell#8>", line 2, in <module>
    if arrs[i] ==None:
IndexError: list index out of range
>>> for i in range(len(arrs)):
	if (arrs[i]) ==None:
		del arrs[i]

		
>>> print(arrs)
[17, 19, 16, 8, 17, 14, 16, 15, 11, 7]
>>> 
