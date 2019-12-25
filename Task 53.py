Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> M =4
>>> def get_count(str):
	vowel=0
	consonant=0
	str=re.sub(r'\d', '', str)
	str=re.sub(r'\w', '', str)
	i=0
	while i < len(str):
		char =str[i]
		if char.lower() in ['a','e','i','o','u','y']:
			vowel+=1
		else:
			consonant+=1
		i+=1
	return vowel, consonant

>>> arrs=[]
>>> for i in range(0,M):
	print("Enter string", end=' ')
	arrs.append(input())

	
Enter string Hello
Enter string Goodbye
Enter string Greetings
Enter string Salutation
>>> for str in arrs:
	vowel =get_count(str)
	consonant=get_count(str)
	print("In string %s there are %s vowels and %s consonants" %(str,vowels,consonant))

	
Traceback (most recent call last):
  File "<pyshell#26>", line 4, in <module>
    print("In string %s there are %s vowels and %s consonants" %(str,vowels,consonant))
NameError: name 'vowels' is not defined
>>> for str in arrs:
	vowel =get_count(str)
	consonant=get_count(str)
	print("In string %s there are %s vowels and %s consonants" %(str,vowel,consonant))

	
In string Hello there are (0, 0) vowels and (0, 0) consonants
In string Goodbye there are (0, 0) vowels and (0, 0) consonants
In string Greetings there are (0, 0) vowels and (0, 0) consonants
In string Salutation there are (0, 0) vowels and (0, 0) consonants
>>> def get_count(str):
	vowel=0
	consonant=0
	str=re.sub(r'\d', '', str)
	i=0
	while i < len(str):
		char =str[i]
		if char.lower() in ['a','e','i','o','u','y']:
			vowel+=1
		else:
			consonant+=1
		i+=1
	return vowel, consonant

>>> arrs=[]
>>> for i in range(0,M):
	print("Enter string", end=' ')
	arrs.append(input())

	
Enter string Hello
Enter string Telephone
Enter string Sphynx
Enter string Jug
>>> for str in arrs:
	vowel,consonant =get_count(str)
	print("In string %s there are %s vowels and %s consonants" %(str,vowel,consonant))

	
In string Hello there are 2 vowels and 3 consonants
In string Telephone there are 4 vowels and 5 consonants
In string Sphynx there are 1 vowels and 5 consonants
In string Jug there are 1 vowels and 2 consonants
>>> 
