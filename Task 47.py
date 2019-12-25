Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> arrs = [random.randint(-10,20) for iter in range(10)]
>>> print(arrs)
[1, 15, 0, 15, 17, -4, -1, -3, 0, -9]
>>> def create_array(arrs,b,c):
	res=[]
	for element in arrs:
		if element>=b:
			if element<=c:
				continue
		res.append(element)
	return res

>>> print(arrs,1,3)
[1, 15, 0, 15, 17, -4, -1, -3, 0, -9] 1 3
>>> 
================================ RESTART: Shell ================================
>>> def create_array(arrs,b,c):
	res=[]
	for element in arrs:
		if element>=b:
			if element<=c:
				continue
		res.append(element)
	return res

>>> arrs =[2,1,0,-1,3,4,-2,4]
>>> print(create_array(arrs,1,3))
[0, -1, 4, -2, 4]
>>> 
