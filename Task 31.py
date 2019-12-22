>>> def bubbleSort(arrs):
	n = len(arrs)
	for i in range(n):
		for j in range(0, n-i-1):
			if arrs[j]>arrs[j+1]:
				arr[j],arrs[j+1] =arrs[j+1], arrs[j]

				
>>> arrs = [1,2,3,4,5,44,221,76,333,9]
>>> bubbleSort(arrs)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    bubbleSort(arrs)
  File "<pyshell#32>", line 6, in bubbleSort
    arr[j],arrs[j+1] =arrs[j+1], arrs[j]
NameError: name 'arr' is not defined
>>> def bubbleSort(arrs):
	n = len(arrs)
	for i in range(n):
		for j in range(0, n-i-1):
			if arrs[j]>arrs[j+1]:
				arrs[j],arrs[j+1] =arrs[j+1], arrs[j]

				
>>> arrs = [1,2,3,4,5,44,221,76,333,9]
>>> bubbleSort(arrs)
>>> for i in range(len(arrs)):
	print("%d" %arrs[i])

	
1
2
3
4
5
9
44
76
221
333
>>> 
