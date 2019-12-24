Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> P=2
>>> 
>>> H=10
>>> list_numbers=[]
>>> sum=0
>>> multiply=1
>>> count=0
>>> while True:
	print("Enter number", end='')
	string=re.sub(r'[^0-9\-]+', '', input())
	if len(string)==0:
		print("Number not found")
		continue
	number = int(string)
	list_numbers.append(number)
	if number<P:
		sum+=number
		elif number>H:
			
SyntaxError: invalid syntax
>>> while True:
	print("Enter number", end='')
	string=re.sub(r'[^0-9\-]+', '', input())
	if len(string)==0:
		print("Number not found")
		continue
	number = int(string)
	list_numbers.append(number)
	if number<P:
		sum+=number
	elif number>H:
		multiply*= number
	if P <H:
		if P<number<H:
			count+=1
	else:
		if H< number<P:
			count+=1
	last_number = list_number[len(list_number)-1]
	if last_number == P or last_number==H:
		break

	
Enter number12
Traceback (most recent call last):
  File "<pyshell#30>", line 19, in <module>
    last_number = list_number[len(list_number)-1]
NameError: name 'list_number' is not defined
>>> while True:
	print("Enter number", end='')
	string=re.sub(r'[^0-9\-]+', '', input())
	if len(string)==0:
		print("Number not found")
		continue
	number = int(string)
	list_numbers.append(number)
	if number<P:
		sum+=number
	elif number>H:
		multiply*= number
	if P <H:
		if P<number<H:
			count+=1
	else:
		if H< number<P:
			count+=1
	last_number = list_numbers[len(list_number)-1]
	if last_number == P or last_number==H:
		break

	
Enter number12
Traceback (most recent call last):
  File "<pyshell#32>", line 19, in <module>
    last_number = list_numbers[len(list_number)-1]
NameError: name 'list_number' is not defined
>>> while True:
	print("Enter number", end='')
	string=re.sub(r'[^0-9\-]+', '', input())
	if len(string)==0:
		print("Number not found")
		continue
	number = int(string)
	list_numbers.append(number)
	if number<P:
		sum+=number
	elif number>H:
		multiply*= number
	if P <H:
		if P<number<H:
			count+=1
	else:
		if H< number<P:
			count+=1
	last_number = list_numbers[len(list_numbers)-1]
	if last_number == P or last_number==H:
		break

	
Enter number12
Enter number34
Enter number12
Enter number55
Enter number2
>>> print("Sum", sum)
Sum 0
>>> print("Multiplication", multiply)
Multiplication 38776320
>>> print("Numbers in range P and H", count)
Numbers in range P and H 0
>>> 
