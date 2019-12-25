Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> M=4
>>> arrs=[]
>>> for i in range(0,M)
SyntaxError: invalid syntax
>>> for i in range(0,M):
	print("Enter string", end=' ')
	arrs.append(input())

	
Enter string Hap py-Fes tive-Sea son
Enter string Mer ry-CH ristmas
Enter string Ha ppy-New Year
Enter string Elem entary
>>> print(' '.join(arrs))
Hap py-Fes tive-Sea son Mer ry-CH ristmas Ha ppy-New Year Elem entary
>>> ar= ' '.join(arrs)
>>> print(ar)
Hap py-Fes tive-Sea son Mer ry-CH ristmas Ha ppy-New Year Elem entary
>>> 
================================ RESTART: Shell ================================
>>> M=4
>>> arrs=[]
>>> for i in range(0,M):
	print("Enter string", end=' ')
	arrs.append(input())

	
Enter string Merry
Enter string Christmas
Enter string Happy
Enter string Holidays
>>> ar= ' '.join(arrs)
>>> print(ar)
Merry Christmas Happy Holidays
>>> 
