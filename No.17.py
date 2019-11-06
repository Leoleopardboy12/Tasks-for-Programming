Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> A = int(input("Side of Cube. "))
Side of Cube. 12
>>> H = int(input("Height of Cylinder. "))
Height of Cylinder. 13
>>> R= int(input("Radius of Cylinder. "))
Radius of Cylinder. 6
>>> M= int(input("Volume of a liquid. "))
Volume of a liquid. 27
>>> if (A**3)>= M:
	print("Possible.")
elif (3.14*R*R*H) >=M:
	print("Possible")
	else:
		
SyntaxError: invalid syntax
>>> if (A**3)>= M:
	print("Possible.")
elif (3.14*R*R*H) >=M:
	print("Possible")
else:
	print("Not possible.")
else:
	
SyntaxError: invalid syntax
>>> if (A**3)>= M:
	print("Possible.")
elif (3.14*R*R*H) >=M:
	print("Possible")
else:
	print("Not possible.")

	
Possible.
>>> 
