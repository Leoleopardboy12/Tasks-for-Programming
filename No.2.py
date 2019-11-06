Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = int(input())
23
>>> b = int(input())
34
>>> c= int(input())
11
>>> if a>b and a>c:
	print(a, "is the Biggest.")
else if b>a and b>c:
	
SyntaxError: invalid syntax
>>> prinif a>b and a>c:
	print(a, "is the Biggest.")
elif b>a and b>c:
	
SyntaxError: invalid syntax
>>> if a>b and a>c:
	print(a, "is the Biggest.")
elif b>a and b>c:
	print(b, "is the Biggest.")
else:
	print(c, "is the Biggest.")

	
34 is the Biggest.
>>> 
