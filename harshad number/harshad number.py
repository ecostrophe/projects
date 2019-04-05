"""
Harshad Number:
A harshad number (or Niven number) is an integer that is divisible by the sum of its digits.
For example:
Input: 18
Output: true (18 is a Harshad number because it is divisible by the sum of its digits: 18 = (1 + 8) x 2)
Input: 1729
Output: true (1729 is a Harshad number because it is divisible by the sum of its digits: 1729 = (1 + 7 + 2 + 9) × 91)
Write a program to check if the user input is a Harshad number or not.
"""
number = input("Enter your number: ")
listnum=[]
sum = 0
harshad = False
harshadnum=[]
for char in number:
	num=int(char)
	listnum.append(num)
	sum += num
		
def harshadnumber(number):
	nivenum = int(number)
	x=0
	while x in range (nivenum+1):
		if sum* x==nivenum:
			harshadnum.append(nivenum)
			break
		else:
			x+=1
	if nivenum in harshadnum:
		print("the input number is: ",nivenum)
		print("the sum of digits: ",sum)
		print(nivenum,"=",sum,"x",x)
		print("So",nivenum,"it's a Harshad number because it is divisible by the sum of its digits. ")
	else:
		print(nivenum,"it's not a Harshad number.")
harshadnumber(number)