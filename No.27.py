Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> A = int(input())
5
>>> if A<=0:
	F=0
	print(F)
elif 0<A<1:
	F=(A*2)-A
	print(F)
else:
	F= (A*2)-sin(3.14*A*2)
	print(F)

	
Traceback (most recent call last):
  File "<pyshell#10>", line 8, in <module>
    F= (A*2)-sin(3.14*A*2)
NameError: name 'sin' is not defined
>>> if A<=0:
	F=0
	print(F)
elif 0<A<1:
	F=(A*2)-A
	print(F)
else:
	import math
	sine = math.sin(3.14*A*2)
	F= (A*2)-sine
	print(F)

	
10.015925862600099
>>> 
