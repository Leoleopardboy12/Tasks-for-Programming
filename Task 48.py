Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> arrs = [random.randint(-10,20) for iter in range(20)]
>>> print(arrs)
[3, 20, -3, -9, 16, 14, -6, 3, 15, -5, -3, 4, 7, -1, -7, -7, 8, 16, 0, -7]
>>> def creat_array(arrs):
	res=[]
	for i in range(len(arrs)):
		if
		
SyntaxError: invalid syntax
>>> def creat_array(arrs):
	res=[]
	for i in range(len(arrs)):
		if i ==0 or i ==1:
			res.append(arrs[i])
		elif arrs[i]==0:
			res.append(arrs[i-1]+arrs[i-2])
		else:
			res.append(arrs[i])
	return res

>>> print(create_array(arrs))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(create_array(arrs))
NameError: name 'create_array' is not defined
>>> print(creat_array(arrs))
[3, 20, -3, -9, 16, 14, -6, 3, 15, -5, -3, 4, 7, -1, -7, -7, 8, 16, 24, -7]
>>> 
