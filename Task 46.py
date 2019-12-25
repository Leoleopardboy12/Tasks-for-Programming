Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> arrs = [random.randint(-10,20) for iter in range(10)]
>>> print(arrs)
[3, 9, 8, -3, -10, 15, 13, 18, 2, 18]
>>> def create_array(arrs,t):
	res=[]
	for element in arrs:
		if element>0:
			res.append(element+element/t)
		else:
			res.append(element)
	return res

>>> print(create_array(arrs,15.0))
[3.2, 9.6, 8.533333333333333, -3, -10, 16.0, 13.866666666666667, 19.2, 2.1333333333333333, 19.2]
>>> 
