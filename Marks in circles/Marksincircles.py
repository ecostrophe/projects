import itertools
matrix=[
	[88,".",8,".",3,".",1,".",8],
	[77,".",22,".",3,".",17,".",1],
	[66,".",22,".",1,".",4,".",3],
	[55,".",2,".",30,".",7,".",4]
]
operations=["+","-","*","/"]
solst=[]
bingoNum=16.0

def slove(row,operations,bingoNum):
	n=0
	cal=0
	getsolst(row,solst,n)
	resultCal=getcal(solst,cal)

	while bingoNum != resultCal:
		n+=1
		getsolst(row,solst,n)
		resultCal=getcal(solst,cal)
	print("variable row",row)
	print("solution list:",solst)
	print("result number:",resultCal)#for test

def getsolst(row,solst,n):
	x=0
	solst.clear()
	op=getoper(operations,n)	
	for i in row:
		if i == ".":
			solst.append(op[x])
			x += 1
		else:
			solst.append(i)
	return solst

def getoper(operations,n):
	oper=list(itertools.permutations(operations,4))
	return oper[n]

def getcal(solst,cal):
	for j in solst:
		posj = solst.index(j)
		if posj==1:
			if j =="+":
				cal = solst[(posj-1)] + solst[(posj+1)]
			elif j =="-":
				cal = solst[(posj-1)] - solst[(posj+1)]
			elif j =="*":
				cal = solst[(posj-1)] * solst[(posj+1)]
			elif j =="/":
				cal = solst[(posj-1)] / solst[(posj+1)]
		else:
			if j =="+":
				cal += solst[(posj+1)]
			elif j =="-":
				cal -= solst[(posj+1)]
			elif j =="*":
				cal *= solst[(posj+1)]
			elif j =="/":
				cal /= solst[(posj+1)]
	return cal


for lst in matrix:
	slove(lst,operations,bingoNum)



