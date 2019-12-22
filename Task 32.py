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
