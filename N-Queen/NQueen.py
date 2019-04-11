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

	for y in range(number):
		for j in range(number):
			grid[y][j]=queen
			if findallposibility(y,j)==True:
				print("===========================")
			else:
				print("there is 0 queen at present")	
#___ fonction creat grid:
def creatgrid():
	global number,case
	row=list(case for x in range(number))
	for i in range(number):
		grid.append(row)
	return True
#___ fonction find all possibility:
sol=[]
def findallposibility(y,j):
	global nextrow,sol
	if 




#__ fonction check posibility:
def checkposibility():
	return
def checkbyrow():
	return
def checkbycol():
	return
slove(number,nqueen)