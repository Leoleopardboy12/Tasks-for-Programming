Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> arrs = [random.randint(-10,20) for iter in range(20)]
>>> print(arrs)
[18, 4, -9, 12, 18, 19, 11, 16, -2, 3, -4, 11, -5, 0, 12, 6, 10, -4, -10, 7]
>>> positive = 0
>>> negative=0
>>> for i in range(len(arrs)):
	if arrs[i]>0:
		positive+=1
	else:
		negative+=1

		
>>> print(positive, negative)
13 7
>>> for i in range(len(arrs)):
	if positive>negative:
		postv= [random.randint(0,20) for iter in range(positive-negative)]
		arrs.append(postv)
	else:
		negv =[random.randint(-10,0) for iter in range(negative-positive)]
		arrs.append(negv)

		
>>> print(arrs)
[18, 4, -9, 12, 18, 19, 11, 16, -2, 3, -4, 11, -5, 0, 12, 6, 10, -4, -10, 7, [0, 5, 11, 7, 16, 7], [9, 1, 15, 8, 14, 7], [12, 13, 13, 0, 18, 5], [2, 1, 14, 13, 15, 5], [15, 9, 19, 3, 0, 16], [10, 12, 15, 8, 16, 17], [5, 12, 9, 5, 10, 11], [19, 20, 1, 4, 10, 11], [2, 18, 10, 17, 6, 12], [2, 16, 3, 7, 10, 18], [14, 8, 6, 9, 3, 9], [7, 9, 3, 17, 7, 7], [20, 18, 19, 12, 1, 1], [0, 9, 8, 13, 3, 5], [1, 3, 12, 1, 18, 20], [7, 1, 20, 5, 5, 5], [10, 12, 6, 16, 4, 1], [6, 1, 14, 11, 18, 0], [3, 8, 10, 16, 3, 9], [17, 0, 14, 20, 18, 15]]
>>> print(len(arrs))
40
>>> if positive>negative:
	postv= [random.randint(0,20) for iter in range(positive-negative)]
		arrs.append(postv)
else:
	negv =[random.randint(-15,-1) for iter in range(negative-positive)]
	arrs.append(negv)
	
SyntaxError: unexpected indent
>>> if positive>negative:
	postv= [random.randint(0,20) for iter in range(positive-negative)]
	arrs.append(postv)
else:
	negv =[random.randint(-15,-1) for iter in range(negative-positive)]
	arrs.append(negv)

	
>>> print(arrs)
[18, 4, -9, 12, 18, 19, 11, 16, -2, 3, -4, 11, -5, 0, 12, 6, 10, -4, -10, 7, [0, 5, 11, 7, 16, 7], [9, 1, 15, 8, 14, 7], [12, 13, 13, 0, 18, 5], [2, 1, 14, 13, 15, 5], [15, 9, 19, 3, 0, 16], [10, 12, 15, 8, 16, 17], [5, 12, 9, 5, 10, 11], [19, 20, 1, 4, 10, 11], [2, 18, 10, 17, 6, 12], [2, 16, 3, 7, 10, 18], [14, 8, 6, 9, 3, 9], [7, 9, 3, 17, 7, 7], [20, 18, 19, 12, 1, 1], [0, 9, 8, 13, 3, 5], [1, 3, 12, 1, 18, 20], [7, 1, 20, 5, 5, 5], [10, 12, 6, 16, 4, 1], [6, 1, 14, 11, 18, 0], [3, 8, 10, 16, 3, 9], [17, 0, 14, 20, 18, 15], [2, 2, 17, 8, 9, 8]]
>>> print(len(arrs))
41
>>> 
================================ RESTART: Shell ================================
>>> import randomarrs = [random.randint(-10,20) for iter in range(20)]
SyntaxError: invalid syntax
>>> import random
>>> arrs = [random.randint(-10,20) for iter in range(20)]
>>> print(arrs)
[7, 11, 1, 19, 1, 4, 12, 16, 8, 7, 14, 19, 19, 9, 4, 12, 17, 15, 15, 0]
>>> positive = 0
>>> negative=0
>>> if positive>negative:
	postv= [random.randint(0,20) for iter in range(positive-negative)]
	arrs.append(postv)
else:
	negv =[random.randint(-15,-1) for iter in range(negative-positive)]
	arrs.append(negv)

	
>>> print(arrs)
[7, 11, 1, 19, 1, 4, 12, 16, 8, 7, 14, 19, 19, 9, 4, 12, 17, 15, 15, 0, []]
>>> 
================================ RESTART: Shell ================================
>>> import random
>>> arrs = [random.randint(-10,10) for iter in range(20)]
>>> print(arrs)
[2, -3, -9, 1, -8, -5, -9, -1, 1, -1, -2, 5, 2, -3, -4, -6, -8, 4, -9, 2]
>>> positive=0
>>> negative=0
>>> for i in range(len(arrs)):
	if arrs[i]>0:
		positive+=1
	else:
		negative+=1

		
>>> if positive>negative:
	postv= [random.randint(0,20) for iter in range(positive-negative)]
	arrs.append(postv)
else:
	negv =[random.randint(-15,-1) for iter in range(negative-positive)]
	arrs.append(negv)

	
>>> print(arrs)
[2, -3, -9, 1, -8, -5, -9, -1, 1, -1, -2, 5, 2, -3, -4, -6, -8, 4, -9, 2, [-13, -2, -15, -1, -1, -15]]
>>> 
================================ RESTART: Shell ================================
>>> import random
>>> arrs = [random.randint(-10,10) for iter in range(20)]
>>> print(arrs)
[1, -5, -6, -7, 4, 8, -3, -8, 1, 7, -10, 8, 9, -6, 7, -5, -9, -2, 8, 5]
>>> positive=0
>>> negative=0
>>> for i in range(len(arrs)):
	if arrs[i]>0:
		positive+=1
	else:
		negative+=1

>>> for positive!= negative:
	
SyntaxError: invalid syntax
>>> while positive!= negative:
	if positive>negative:
		
		negv =[random.randint(-15,-1) for iter in range(negative-positive)]
		arrs.append(negv)
		negative+=1
	else:
		postv= [random.randint(0,20) for iter in range(positive-negative)]
		arrs.append(postv)
		positive+=1

		
>>> print(arrs)
[1, -5, -6, -7, 4, 8, -3, -8, 1, 7, -10, 8, 9, -6, 7, -5, -9, -2, 8, 5]
>>> print(len(arrs))
20
>>> 
