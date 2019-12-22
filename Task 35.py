Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> M= 5
>>> K=3
>>> P=5
>>> arrs = [1,2,3,4,5,6,7,8,11,22,33,21]
>>> A = arrs[lens(arrs[M]))
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> A = arrs[lens(arrs[M])]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    A = arrs[lens(arrs[M])]
NameError: name 'lens' is not defined
>>> A = arrs[len(arrs[M])]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    A = arrs[len(arrs[M])]
TypeError: object of type 'int' has no len()
>>> A = len(arrs[M])
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    A = len(arrs[M])
TypeError: object of type 'int' has no len()
>>> A = arrs[0,P]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    A = arrs[0,P]
TypeError: list indices must be integers or slices, not tuple
>>> A = arrs[0:P]
>>> print(A)
[1, 2, 3, 4, 5]
>>> A = arrs[0:M]
>>> A= arrs[K:M]
>>> A= arrs[K:5]
>>> B=arrs[P:5]
>>> print(A, B)
[4, 5] []
>>> for i in range(len(arrs)):
	A= arrs[K:K+M]
KeyboardInterrupt
>>> A= arrs[K:K+M]
>>> B = arrs[P:P+M]
>>> arrs = [B+A]
>>> print(arrs)
[[6, 7, 8, 11, 22, 4, 5, 6, 7, 8]]
>>> 
