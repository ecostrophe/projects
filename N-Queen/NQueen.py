case="-"
queen="Q"
nqueen=0
nextrow=[]
grid=[]
number=int(input("Please enter the number of queen:\n"))
def slove(number,nqueen):
	if creatgrid() == True:
		for item in grid:
			print(item)
	else:
		print("there is no grid created")
		
	if findallposibility(grid):
		print(nextrow)
	else:
		print("there is 0 queen at present")
		
#___ fonction creat grid:
def creatgrid():
	global number,case
	row=list(case for x in range(number))
	for i in range(number):
		grid.append(row)
	return True
	
#___ fonction find all posibility:
sol=[]
def findallposibility(grid):
	global nextrow
	for x in grid:
		if x.index(queen)==0:
			nextrow=x.copy()
			nextrow.remove(x[1])
			nextrow.remove(x[0])
			return nextrow
		elif x.index(queen)==(number-1):#_____
			nextrow=x.copy()
			nextrow.remove(x[-2])
			nextrow.remove(x[-1])
			return nextrow
		else:
			return nextrow
	else:
		return True
#__ fonction check posibility:
def checkposibility():
	return
def checkbyrow():
	return
def checkbycol():
	return
slove(number,nqueen)