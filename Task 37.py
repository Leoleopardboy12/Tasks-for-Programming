Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> arrs.randint(0,10)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    arrs.randint(0,10)
NameError: name 'arrs' is not defined
>>> import random
>>> arrs = [random.randint(0,12) for iter in range(10)]
>>> print(arrs)
[3, 11, 5, 11, 8, 11, 1, 11, 10, 4]
>>> sum(arrs)
75
>>> Sum = sum(arrs)
>>> for in range(lens(arrs)):
	
SyntaxError: invalid syntax
>>> for i in range(lens(arrs)):
	if (arrs[i]%2)==0:
		evn_num+=1

		
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    for i in range(lens(arrs)):
NameError: name 'lens' is not defined
>>> for i in range(len(arrs)):
	if (arrs[i]%2)==0:
		evn_num+=1

		
Traceback (most recent call last):
  File "<pyshell#12>", line 3, in <module>
    evn_num+=1
NameError: name 'evn_num' is not defined
>>> evn = 0
>>> for i in range(len(arrs)):
	if (arrs[i]%2)==0:
		evn+=1

		
>>> print(evn)
3
>>> arrs.insert(0, Sum)
>>> arrs.insert(1, evn)
>>> print(arrs)
[75, 3, 3, 11, 5, 11, 8, 11, 1, 11, 10, 4]
>>> 
