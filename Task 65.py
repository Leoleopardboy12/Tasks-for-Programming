Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> list_numbers=[]
>>> B =5
>>> sum=0
>>> while True:
	print("Enter number:", end=' ')
	string = re.sub(r'[^0-9\-]+', ' ', input())
	if len(string) == 0:
		print("Number not found")
		continue
	num= int(string)
	list_number.append(num)
	if num<0:
		break
	if num%B ==0:
		sum+=num

		
Enter number: 25
Traceback (most recent call last):
  File "<pyshell#15>", line 8, in <module>
    list_number.append(num)
NameError: name 'list_number' is not defined
>>> while True:
	print("Enter number:", end=' ')
	string = re.sub(r'[^0-9\-]+', ' ', input())
	if len(string) == 0:
		print("Number not found")
		continue
	num= int(string)
	list_numbers.append(num)
	if num<0:
		break
	if num%B ==0:
		sum+=num

		
Enter number: 12
Enter number: 25
Enter number: 20
Enter number: 34
Enter number: 5
Enter number: -25
>>> print("Sum", sum)
Sum 50
>>> 
