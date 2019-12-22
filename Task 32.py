Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> arrs = [1,4,56,7,71,12,76,3,9]
>>> def bubbbleSort(arrs):
	n = len(arrs)

	
>>> def bubbbleSort(arrs):
	n = len(arrs)
	for i in range(n):
		for j in range(0, n-i-1):
			if (arrs[j]%2)==0:
				if (arrs[j+1]%3)==0:
					arrs[j], arrs[j+1] = arrs[j+1], arrs[j]

>>> bubbleSort(arrs)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    bubbleSort(arrs)
NameError: name 'bubbleSort' is not defined
>>> arrs = [1,4,56,7,71,12,76,3,9]
>>> bubbleSort(arrs)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    bubbleSort(arrs)
NameError: name 'bubbleSort' is not defined
>>> bubbbleSort(arrs)
>>> for i in range(len(arrs)):
	print("%d" %arrs[i])

	
1
4
56
7
71
3
9
12
76
>>> def bubbbleSort(arrs):
	n = len(arrs)
	for i in range(n):
		for j in range(0, n-i-1):
			if (arrs[j]%3)==0:
				if (arrs[j+1]%2)==0:
					arrs[j], arrs[j+1] = arrs[j+1], arrs[j]

					
>>> bubbbleSort(arrs)
>>> for i in range(len(arrs)):
	print("%d" %arrs[i])

	
1
4
56
7
71
76
12
3
9
>>> def bubbbleSort(arrs):
	n = len(arrs)
	for i in range(n):
		for j in range(0, n-i-1):
			if (arrs[j]%3)==0:
				if (arrs[j+1]%2)==0:
					arrs[j], arrs[j+1] = arrs[j+1], arrs[j]
			elif(arrs[j]%2)==0:
				if (arrs[j+1]%3)==0:
					arrs[j], arrs[j+1] = arrs[j+1], arrs[j]

					
>>> bubbbleSort(arrs)
>>> for i in range(len(arrs)):
	print(arrs[i])

	
1
4
56
7
71
12
3
9
76
>>> 
============================================================================ RESTART: Shell ===========================================================================
>>> def bubbbleSort(arrs):
	n = len(arrs)
	for i in range(n):
		for j in range(0, n-i-1):
			if (arrs[j]%3)==0:
				if (arrs[j+1]%2)==0:
					arrs[j], arrs[j+1] = arrs[j+1], arrs[j]

					
>>> arrs = [1,2,3,4,5,6,7,8,9]
>>> bubbbleSort(arrs)
>>> for i in range(len(arrs)):
	print(arrs[i])

	
1
2
4
3
5
6
7
8
9
>>> 
============================================================================ RESTART: Shell ===========================================================================
>>> def bubbbleSort(arrs):
	n = len(arrs)
	for i in range(n):
		for j in range(0, n-i-1):
			if (arrs[j]%2)!=0:
				if (arrs[j+1]%2)==0:
					arrs[j], arrs[j+1] = arrs[j+1], arrs[j]

					
>>> arrs = [1,4,56,7,71,12,76,3,9]
>>> bubbbleSort(arrs)
>>> for i in range(len(arrs)):
	print(arrs[i])

	
4
56
12
76
1
7
71
3
9
>>> 
