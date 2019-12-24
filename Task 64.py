Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> list_numbers=[]
>>> sum=0
>>> while True:
	print("Enter number:", end=' ')
	string = re.sub(r'[^0-9\-]+', '', input())
	if len(string) ==0:
		print("Number not found")
		continue
	number = int(string)
	list_number.append(number)
	if number ==99999:
		break
	elif number ==0:
		print("Sum", sum)
	else:
		sum+=number

		
Enter number: 1
Traceback (most recent call last):
  File "<pyshell#17>", line 8, in <module>
    list_number.append(number)
NameError: name 'list_number' is not defined
>>> while True:
	print("Enter number:", end=' ')
	string = re.sub(r'[^0-9\-]+', '', input())
	if len(string) ==0:
		print("Number not found")
		continue
	number = int(string)
	list_numbers.append(number)
	if number ==99999:
		break
	elif number ==0:
		print("Sum", sum)
	else:
		sum+=number

		
Enter number: 1
Enter number: 2
Enter number: 3
Enter number: 4
Enter number: 5
Enter number: 6
Enter number: 6
Enter number: 7
Enter number: 8
Enter number: 445
Enter number: 776
Enter number: 2
Enter number: 
Number not found
Enter number: 99999
>>> print("Sum:", sum)
Sum: 1265
>>> 
