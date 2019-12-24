Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> list_numbers=[]
>>> sum=0
>>> sim_count=0
>>> multiply=1
>>> multiply_sum=0
>>> i=1
>>> while True:
	print("Enter number", end=' ')
	string = re.sub(r'\D', '', input())
	if len(string)==0:
		print("Number not found")
		continue
	number = int(string)
	list_numbers.append(number)
	if i%2 !=0:
		sum+= number
		sim_count+=1
	else:
		multiply = multiply*number
		multiply_sum+=1
	i+=1
	if list_numbers[len(
KeyboardInterrupt
>>> if list_numbers[len(list_numbers)-1== 55555:
		break
		
SyntaxError: invalid syntax
>>> while True:
	print("Enter number", end=' ')
	string = re.sub(r'\D', '', input())
	if len(string)==0:
		print("Number not found")
		continue
	number = int(string)
	list_numbers.append(number)
	if i%2 !=0:
		sum+= number
		sim_count+=1
	else:
		multiply = multiply*number
		multiply_sum+=1
	i+=1
	if list_numbers[len(list_numbers)-1]==55555:
		break

	
Enter number 23
Enter number 33
Enter number 44
Enter number 44
Enter number 55
Enter number 66
Enter number 77
Enter number 88
Enter number 1
Enter number 2
Enter number 3
Enter number 4
Enter number 5
Enter number 6
Enter number 7
Enter number 8
Enter number 9
Enter number 9
Enter number 08
Enter number 7
Enter number 6
Enter number 5
Enter number 555
Enter number 55555
>>> print("Sum", sum)
Sum 793
>>> print("Sum count", sim_count)
Sum count 12
>>> print("Multipe", multiply)
Multipe 56670644807884800
>>> print("Sum of Miltiplication", sum_multiply)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print("Sum of Miltiplication", sum_multiply)
NameError: name 'sum_multiply' is not defined
>>> print("Sum of Miltiplication", multiply_sum)
Sum of Miltiplication 12
>>> 
