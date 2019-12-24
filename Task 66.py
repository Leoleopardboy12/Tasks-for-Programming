Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> list_numbers=[]
>>> positive_count
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    positive_count
NameError: name 'positive_count' is not defined
>>> positive_count=0
>>> negative_count=0
>>> while True:
	print("Enter number:", end=' ')
        string = re.sub(r'[^0-9\-]+', ' ', input())
	if len(string) == 0:
		print("Number not found")
		continue
	
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> while True:
	print("Enter number:", end=' ')
	string = re.sub(r'[^0-9\-]+', ' ', input())
	if len(string) == 0:
		print("Number not found")
		continue

	
Enter number: 
================================ RESTART: Shell ================================
>>> import re
>>> list_numbers=[]
>>> positive_count=0
>>> negative_count=0
>>> while True:
	print("Enter number:", end=' ')
	string = re.sub(r'[^0-9\-]+', ' ', input())
	if len(string) == 0:
		print("Number not found")
		continue
	num = int(string)
	if num * == -65432:
		
SyntaxError: invalid syntax
>>> while True:
	print("Enter number:", end=' ')
	string = re.sub(r'[^0-9\-]+', ' ', input())
	if len(string) == 0:
		print("Number not found")
		continue
	num = int(string)
	if num == -65432:
		break
	list_numbers.append(num)
	if number<0:
		negative_count +=1
	else:
		positive_count+=1

		
Enter number: 23
Traceback (most recent call last):
  File "<pyshell#24>", line 11, in <module>
    if number<0:
NameError: name 'number' is not defined
>>> while True:
	print("Enter number:", end=' ')
	string = re.sub(r'[^0-9\-]+', ' ', input())
	if len(string) == 0:
		print("Number not found")
		continue
	num = int(string)
	if num == -65432:
		break
	list_numbers.append(num)
	if num<0:
		negative_count +=1
	else:
		positive_count+=1

		
Enter number: 12
Enter number: 34
Enter number: 56
Enter number: 87
Enter number: -23
Enter number: -45
Enter number: 
Number not found
Enter number: -65432
>>> 1_percent=100/len(list_numbers)
SyntaxError: invalid decimal literal
>>> one_percent=100/len(list_numbers)
>>> print("Percentage of Positves", one_percent*positive_count)
Percentage of Positves 57.142857142857146
>>> print("Percentage of Negatives", one_percent*negative_count)
Percentage of Negatives 28.571428571428573
>>> 
