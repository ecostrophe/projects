#!/usr/bin/python
vowels=["a","e","i","o","u"]
word= input("enter your word: ").lower()
counter=[]
for char in word:
    if char in vowels:
    counter.append(char)
print("There is: ",len(counter),"vowel(s) in your word (",word,")")
for v in vowels:
    if v in counter:
    print ("- The", v," vowel ",counter.count(v))