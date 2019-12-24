Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> list_numbers=[]
>>> sum = 0
>>> sum_count = 0
>>> i = 1
>>> while True:
	print("Enter number:", end=' ')
	string = re.sub(r'[^0-9\-]+', ' ', input())
	if len(string) == 0:
		print("Number not found")
		continue
	number = int(string)
	list_numbers.append(number)
	if i%2 !=0:
		number*=-1
	else:
		number*=number
	sum +=number
	i+=1
	if list_numbers[len(list_numbers)-1]<0:
		break

	
Enter number: 1
Enter number: 2
Enter number: 3
Enter number: 4
Enter number: 5
Enter number: 
Number not found
Enter number: 6
Enter number: 44
Enter number: 23
Enter number: 1000
Enter number: 0
Enter number: -1
>>> print("Sum", sum)
Sum -467
>>> print("Number of terms", i)
Number of terms 12
>>> 
