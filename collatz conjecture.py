"""The Collatz conjecture (also known as the Ulam conjecture or the Syracuse problem) is an unsolved mathematical problem, which is very easy to formulate:
1. Take any natural number
2. If it's even, half it, otherwise triple it and add one
3. Repeat step 2. until you reach 4, 2, 1 sequence
4. You will ALWAYS reach 1, eventually.
That last sequence: 4, 2, 1 is an infinitely repeating loop. The formulated conjecture is that for any x the sequence will always reach 4, 2, 1 ultimately.
While the problem cannot be proved, the assignment is to write a code that will produce and print out the whole sequence for an input number."""

number=int(input("Please enter any natural number!!\n"))
print("The collatz conjecture the number: ",number)
halfcount=0
triplecount=0
while number !=1:
	if number%2==0:
		number=int(number/2)
		print(number)
		halfcount+=1
	else:
		number=int((number*3)+1)
		print(number)
		triplecount+=1
total=halfcount+triplecount
print("---- Information about the current Collatz Conjecture: ----")
print("-We used:",total,"sequences for this number.")
print("-For Half method we used:",halfcount,"times. With:(",int((halfcount*100)/total),"%)")
print("-For Tripling and adding one method we used:",triplecount,"times. With:(",int((triplecount*100)/total),"%)")
print("-----------------------------------------------------------")
