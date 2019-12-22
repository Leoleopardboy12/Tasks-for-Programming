Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> arrs = [random.randint(-10,20) for iter in range(20)]
>>> print(arrs)
[9, 20, 8, 4, 19, 6, -3, -3, 11, 4, 20, 0, 16, 15, 17, 14, 0, 19, 5, 7]
>>> for i in range(len(arrs)):
	arrs.split(arrs[i]>0, -1)

	
Traceback (most recent call last):
  File "<pyshell#6>", line 2, in <module>
    arrs.split(arrs[i]>0, -1)
AttributeError: 'list' object has no attribute 'split'
>>> for i in range(len(arrs)):
	arrs.split(arrs[i]>0, -1)

	
Traceback (most recent call last):
  File "<pyshell#8>", line 2, in <module>
    arrs.split(arrs[i]>0, -1)
AttributeError: 'list' object has no attribute 'split'
>>> 
>>> 
================================ RESTART: Shell ================================
>>> import random
>>> arrs = [random.randint(-10,20) for iter in range(20)]
>>> print(arrs)
[3, 10, -4, 7, 8, 5, 5, 20, 6, 6, 7, 15, 1, 12, 13, -7, 3, -10, 18, 0]
>>> positive_list =[]
>>> negative_list = []
>>> for i in range(len(arrs)):
	if arrs[i]>0:
		positive_list.append(arrs[i])
	else:
		negative_list.append(arrs[i])

		
>>> print(positive_list)
[3, 10, 7, 8, 5, 5, 20, 6, 6, 7, 15, 1, 12, 13, 3, 18]
>>> print(negative_list)
[-4, -7, -10, 0]
>>> 
