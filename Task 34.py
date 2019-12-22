
>>> arrs = [1,2,3,4,5,6,7,8]
>>> A = arrs[:len(arrs)//2]
>>> B= arrs[len(arrs)//2:]

>>> arrs=[B+A]
>>> for i in range(len(arrs)):
	print(arrs[i])

	
[5, 6, 7, 8, 1, 2, 3, 4]
>>> 
