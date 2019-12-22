Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> arrs = [random.randint(-10,20) for iter in range(20)]
>>> print(arrs)
[16, -8, 9, 17, 16, -5, 14, 14, -5, -2, -2, 9, 11, 6, 19, -3, 20, 1, -1, 7]
>>> for i in range(len(arrs)):
	if arrs[i]==0:
		if arrs[i+1]==0:
			print(arrs[i], arrs[i+1])

			
>>> 
>>> consec_zeros= None
>>> for i in range(len(arrs)):
	if arrs[i]==0:
		if arrs[i+1]==0:
			consec_zeros=1

			
>>> if consec_zeros>0:
	print("There are consecutive zeros.")
else:
	print("There are NO cosecutive zeros.")

	
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    if consec_zeros>0:
TypeError: '>' not supported between instances of 'NoneType' and 'int'
>>> consec_zeros= 0
>>> for i in range(len(arrs)):
	if arrs[i]==0:
		if arrs[i+1]==0:
			consec_zeros=1

			
>>> if consec_zeros>0:
	print("There are consecutive zeros.")
else:
	print("There are NO cosecutive zeros.")

	
There are NO cosecutive zeros.
>>> 
