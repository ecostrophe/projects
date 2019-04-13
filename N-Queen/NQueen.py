case="-"
queen="Q"
nqueen=0
sol=[]
grid=[]
number=int(input("Please enter the number of queen:\n"))
def slove(number,nqueen):
	if creatgrid() == True:
		print("creation of grid of N-Queen Problem for N=",number) # text for test only
		for item in grid:
			print(item)
	if findallposibility(grid):
		print("creation of grid with possible Queen positions") #text for test only
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
	global queen, case, nqueen, sol
	for row in grid:
		for z in range (number):
			row[z]=queen
			checkbyrow(row)
			if checkbyrow(row):
				nqueen+=1
			else:
				row[z]=case
	return sol
#__ fonction to check evry row in grid
def checkbyrow(row):
	global sol,queen,case
	if len(sol)==0:
		sol.append(row)
		return True
	else:
		for prop in sol:
			if row.index(queen)== prop.index(queen):
				return False
			else:
				return True


# fonction to check evry column in grid
def checkbycol():
	return
#__ fonction check posibility:
def checkposibility():
	return

slove(number,nqueen)