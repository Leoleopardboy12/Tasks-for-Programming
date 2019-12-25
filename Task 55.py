Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> M=3
>>> arrs=[]
>>> for i in range(0,M):
	print("Enter string", end=' ')
	arrs.append(input())

	
Enter string 5432
Enter string 65432
Enter string 123
>>> print("Enter word", end=' ')
Enter word 
>>> Word
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    Word
NameError: name 'Word' is not defined
>>> print("Enter word", end=' ')
Enter word 
>>> syllable = input()
Word
>>> for string in arrs:
	string = re.sub(syllable, '', string)
	print(string)

	
5432
65432
123
>>> 
