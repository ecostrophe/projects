"""The Caesar cipher is a type of substitution cipher in which each letter in the plaintext is shifted to a certain number of places down the alphabet. For example, with a shift of 1, A would be replaced by B, B would become C, and so on. The method is named after Julius Caesar, who allegedly used it to communicate with his generals.
For example:
Input: "defend the east wall of the castle"
Output: "efgfoe uif fbtu xbmm pg uif dbtumf"""
import string
letters=list(string.ascii_lowercase)
punctuations=(string.punctuation)
digits=list(string.digits)
wordsin=input("Please enter your words:\n").lower()
cryptdic={}
words=[]
digi=1
for letter in letters:
	cryptdic[letter]=(digi)
	digi+=1
	
for char in wordsin:
	if char=="z":
		key= list(cryptdic.keys())[0]
		words.append(key)
	elif char==" ":
		words.append(char)
	elif char in punctuations:
		words.append(char)
	elif char in digits:
		words.append(char)
	else:
		key= list(cryptdic.keys())[cryptdic[char]]
		words.append(key)
sp=""
print(sp.join(words))