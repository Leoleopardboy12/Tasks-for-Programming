Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = int(input("Enter integer. "))
Enter integer. 100
>>>  if (x % 2) ==0:
	print(x, "is even.")
else:
	print(x, "is Odd")
	
SyntaxError: unexpected indent
>>> if (x % 2) ==0:
	print(x, "is even.")
else:
	print(x, "is Odd")

	
100 is even.
>>> if (x % 10) ==0:
	print(x, "is not a multiple of 4")
else:
	print("It is not")

	
100 is not a multiple of 4
>>> if (x % 10) ==0:
	print(x, "is not a multiple of 10")
else:
	print("It is not")

	
100 is not a multiple of 10
>>> if (x % 10) ==0:
	print(x, "is a multiple of 10")
else:
	print("It is not")

	
100 is a multiple of 10
>>> 
