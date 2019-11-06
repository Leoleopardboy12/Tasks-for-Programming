Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=int(input())
22
>>> if x >0:
	print(x)
elif:
	
SyntaxError: invalid syntax
>>> if x >0:
	print(x)
	elif:
		
SyntaxError: invalid syntax
>>> if x >0:
	print(x)
elif x==0:
	print("Zero")
else:
	print(x,"Negative.")

	
22
>>> if x >0:
	print(x,"Positive")
elif x==0:
	print("Zero")
else:
	print(x,"Negative.")

	
22 Positive
>>> 
