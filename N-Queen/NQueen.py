case="-"
queen="Q"
nqueen=0
sol=[]
grid=[]
number=int(input("Please enter the number of queen:\n"))
def slove(number,nqueen):
	if creatgrid() == True:
		print("Creation of empty grid of N-Queen Problem for N=",number) # text for test only
		for item in grid:
			print(item)

	if findallposibility(grid):
		print("Creation of grid with possible Queen positions with",nqueen,"Queen(s)") #text for test only
		for item in sol:
			print(item)
	
#___ fonction creat grid:
def creatgrid():
	global number,case
	row=list(case for x in range(number))
	for i in range(number):
		grid.append(row)
	return True
#___ fonction find all possibility:
def findallposibility(grid):
	global queen, case, nqueen,sol
	for row in grid:
		for z in range (number):
			row[z]=queen
			print("the row sending to check by row fonction is:",row)#for test only
			gt= checkbyrow(row)
			print ("result of the check by row fonction is:",gt)#for test only
			if checkbyrow(row):
				nqueen+=1
				print("the number of queen is found are:",nqueen)#for test only
			else:
				row[z]=case
	return True



#__ fonction to check evry row in grid
def checkbyrow(row):
	global sol,grid
	print("the sol liste:",sol)#for test only
	if len(sol)==0:
		sol.append(row)
		return True
	else:
		if row in sol:
			return False
		else:
			sol.append(row)
			return True

#__ fonction check posibility:
def checkposibility():
	return

slove(number,nqueen)