Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> arrs = [random.randint(-10,20) for iter in range(20)]
>>> print(arrs)
[12, 2, -3, 3, -2, -2, -4, 12, 13, 6, 1, 2, 8, 18, 14, 20, 2, 0, 1, 6]
>>> three_divisible=0
>>> for i in range(len(arrs)):
	if (arrs[i]%3)==0:
		three_divisible+=1

		
>>> print(three_divisible)
8
>>> evn_avg=0
>>> total_evn=0
>>> for i in range(len(arrs)):
	if (arrs[i]%2)==0:
		total_evn+=1
		evn_avg=evn_avg + arrs[i]

		
>>> average=evn_avg/total_evn
>>> print(average)
6.266666666666667
>>> arrs.insert(0, three_divisible)
>>> arrs.insert(-1, average)
>>> print(arrs)
[8, 12, 2, -3, 3, -2, -2, -4, 12, 13, 6, 1, 2, 8, 18, 14, 20, 2, 0, 1, 6.266666666666667, 6]
>>> 
