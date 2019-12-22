Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> arrs = [random.randint(0,12) for iter in range(10)]
>>> K==5
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    K==5
NameError: name 'K' is not defined
>>> K=5
>>> arrs.del(K:-1)
SyntaxError: invalid syntax
>>> del arrs[K:-1]
>>> print(arrs)
[8, 12, 9, 6, 3, 12]
>>> 
================================ RESTART: Shell ================================
>>> import random
>>> arrs = [random.randint(0,12) for iter in range(10)]
>>> print(arrs)
[6, 10, 8, 8, 9, 8, 12, 0, 6, 1]
>>> K=7
>>> del arrs[K:-1]
>>> print(arrs)
[6, 10, 8, 8, 9, 8, 12, 1]
>>> del arrs[K:]
>>> print(arrs)
[6, 10, 8, 8, 9, 8, 12]
>>> 
