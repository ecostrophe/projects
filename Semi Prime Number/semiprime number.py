""""
A semiprime number is a natural number that is the product of exactly two (not necessarily distinct) primes. For that I creat this program to check if the user input is a semiprime number or not.
"""
number= int(input("Enter your number: "))
dividingnum=[]
primenum=[]
semiprimenum=[]
def numberprime(number):
	num=1
	prime=1
	semiprime=False
	while num <= number:
		for x in range (number):
			x+=1
			for n in range (number):
				n+=1
				if x%n==0:
					num+=1
					dividingnum.append(x)
				else:
					num+=1
	while prime <= number:
		if dividingnum.count(prime)<=2:
			primenum.append(prime)
			prime+=1
		else:
			prime+=1
	while semiprime is False:
		for prime1 in primenum:
			for prime2 in primenum:
				if prime1 * prime2 == number:
					semiprimenum.append(number)
					semiprime = True
					print(semiprime, number, "is a semiprime number because it is product of two prime numbers:",prime1,"x",prime2)
		if number not in semiprimenum:
			print(semiprime, number, "is not a semiprime number")
			semiprime = True
numberprime(number)

