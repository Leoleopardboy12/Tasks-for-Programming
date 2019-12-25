Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> M=2
>>> arrs=[]
>>> for i in range(0,M):
	print("Enter string", end=' ')
	arrs.append(input())

	
Enter string just
Enter string programming
>>> print("Enter word", end=' ')
Enter word 
>>> syllable = input()
Gaming
>>> for string in arrs:
	count = len(re.findall(syllable, string))
	print("In string \%s\" the word \"%s\" is met \"%s\" times." % (string,syllable, count))

	
In string \just" the word "Gaming" is met "0" times.
In string \programming" the word "Gaming" is met "0" times.
>>> 
