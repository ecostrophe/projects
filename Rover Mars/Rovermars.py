import random
import time
time.sleep(3)
print("Please wait while connecting to NASA-Sat ......")
time.sleep(2)
print("Now we are connecting to the Rover Mars Machine Via NASA-Sat.")
rpm=str(input("\nHello Earth Base Control from Mars plante :)\nI am the assitante of the rover Thissnath ;) \nPlease entre CMD command to activate the The Remote Processing Model:\n")).upper()
listcmd =[]
if rpm == "CMD":
	print("\nThe Remote Processing Model Mode is activate.")
	listcmd.append(rpm)
else:
	print("Auto Rover Remote Mode is activate.")
	
class Rovermars():
	def __init__(self,name,model,position,energy,domage,stock,capacity,memory,signal):
		self.name = name
		self.model = model
		self.position = position
		self.energy = energy
		self.domage = domage
		self.stock = stock
		self.capacity = capacity
		self.memory = memory
		self.signal = signal
	def __str__(self):
		return "\n*** The Rover Mars Information: ***\n- Name: "+ self.name+"\n- Model: "+ self.model +"\n- Position: "+str(self.position)+"\n- Energy: "+ str(self.energy)+"%"+"\n- Domage: "+str(self.domage)+"\n- Stock: "+str(self.stock)+"\n- Capacity: "+str(self.capacity)+"Kg"+"\n- Memory: "+str(self.memory)+"/10 Pics"+"\n- Signal: "+str(self.signal)+"/5"+"\n***********************************"
		
	def remoterover(self, remote= False):
		if rpm == "CMD":
			remote = True
			while remote is True:
				print("\n*** The Rover Mars Information: ***\n- Name: "+ self.name+"\n- Model: "+ self.model +"\n- Position: "+str(self.position)+"\n- Energy: "+ str(self.energy)+"%"+"\n- Domage: "+str(self.domage)+"\n- Stock: "+str(self.stock)+"\n- Capacity: "+str(self.capacity)+"Kg"+"\n- Memory: "+str(self.memory)+"/10 Pics"+"\n- Signal: "+str(self.signal)+"/5"+"\n***********************************")
				print("\n*** The Command List: ***\n- MOV F or MOV B  :(for move the rover to the Forward or the Back position).\n- TUR L or TUR R : (for turn the rover to the Left or to the Right).\n- RCK : (for collecting objects).\n- RLS : (for cleaning and relasing the rover).\n- ANL : (for analyise the last collected object).\n- PIC : (to take picture to the area).\n- LOG : (to print a list of all command)\n___________________________\n")
				command = str(input("please entre your command: ")).upper()
				listcmd.append(command)
				p0,p1,p2=[5,-5],[6,-6,7,-7,8,-8,9,-9],[10,-10,11,-11,12,-12]
				chance = random.randint(0,100)
				if self.signal == 0 and chance >=20:
					print("chance: ", chance)#test
					print("NASA-Sat lose connection with the rover "+ self.name +" .....")
					return remote is False
				elif self.signal == 1:
					print("From the rover "+self.name+" to Earth Base Control you must return to the connection zone!!")

				if self.energy <= 0:
					print("The rover battery is very low try to connecting after now!!")
					return remote is False
				elif self.energy <= 10:
					print("the rover battery is low !!")

				if self.domage >= 80:
					print("you must relase the rover !!")
				elif self.domage >= 100:
					print("The rover is broken !!")
					return remote is False

				if command == "MOV F":
					self.position[1] +=1
					self.domage+=5
					self.energy-= 5
					if self.position[1] in p0:
						self.signal-=1
						print("the rover "+self.name+" move to the position: ",self.position)						
					elif self.position[1] in p1:
						self.signal=random.randint(1,3)
						print("the rover "+self.name+" move to the position: ",self.position)
					elif self.position[1] in p2:
						self.signal = 0
						print("the rover "+self.name+" move to the position: ",self.position)
					else:
						self.signal = 5
				elif command == "MOV B":
					self.position[1] -=1
					self.domage+=5
					self.energy -= 5
					if self.position[1] in p0:
						self.signal-=1
						print("the rover "+self.name+" move  back to the position: ",self.position)
					elif self.position[1] in p1:
						self.signal=random.randint(1,3)
						print("the rover "+self.name+" move  back to the position: ",self.position)
					elif self.position[1] in p2:
						self.signal = 0
						print("the rover "+self.name+" move  back to the position: ",self.position)
					else:
						self.signal = 5

				elif command == "TUR L":
					self.position[0] -=1
					self.domage+=5
					self.energy -= 5
					if self.position[0] in p0:
						self.signal-=1
						print("the rover "+self.name+" turn  left to the position: ",self.position)
					elif self.position[0] in p1:
						self.signal=random.randint(1,3)
						print("the rover "+self.name+" turn  left to the position: ",self.position)
					elif self.position[0] in p2:
						self.signal = 0
						print("the rover "+self.name+" turn  left to the position: ",self.position)
					else:
						self.signal = 5

				elif command == "TUR R":
					self.position[0] +=1
					self.domage+=5
					self.energy -= 5
					if self.position[0] in p0:
						self.signal-=1
						print("the rover "+self.name+" turn  right to the position: ",self.position)
					elif self.position[0] in p1:
						self.signal=random.randint(1,3)
						print("the rover "+self.name+" turn  right to the position: ",self.position)
					elif self.position[0] in p2:
						self.signal = 0
						print("the rover "+self.name+" turn  right to the position: ",self.position)
					else:
						self.signal = 5

				elif command == "RCK":
					return self.collectObject(i)
					
				elif command == "RLS":
					return self.relaseRover()
					
				elif command == "ANL":
					return self.analyzeObject(i)

				elif command == "PIC":
					return self.takePic()
				
				elif command == "LOG":
					return self.viewlog()
				else:
					return
		else:
			print ("So sorry you can't remote the rover manuely")
			return remote is False

	def collectObject(self,i):
		if self.position == i.getposition() and self.capacity >= i.getweight():
			self.stock.append(i.getname())
			self.domage += 5
			self.energy -= 5
			self.capacity -= i.getweight()
			print("Object called "+i.getname()+" is collected")
			return self.remoterover()
		elif self.position == i.getposition() and self.capacity <= i.getweight():
			print("This object is very big and heavy to put it in the stock")
			return self.remoterover()
		else:
			print("Sorry, there is no object here to collecte it!!")
			return self.remoterover()

	def relaseRover(self):
		time=0
		self.energy+=25
		self.domage-=20
		time+=1
		print("\nThe rover is cleaning for",time," time(s)")
		print("The rover "+self.name+" is relase and charge some battery.")
		return self.remoterover()
		
	def analyzeObject(self,i):
		time.sleep(2)
		if i.getname() in self.stock and self.energy>=20:
			self.energy -=20
			self.stock.remove(i.getname())
			self.domage += 5
			self.energy -= 10
			self.capacity += i.getweight()
			print("analyze of object :", i.getname(), " is done ",i.getingredient())
			return self.remoterover()
		elif i.getname() not in self.stock and self.energy>=20:
			print("There is no things in your Stock to analyze it!!")
			return self.remoterover()
		elif i.getname() in self.stock and self.energy<=20:
			print("unless Energy to analyze the object")
			return self.remoterover()
		else:
			print("sorry check your command!!")
			return self.remoterover()

	def takePic(self):
		self.memory -=1
		self.energy -=3
		print("the rover "+self.name+" take a picture to area")
		piccmd= str(input("To view the picture entre VIW command:")).upper()
		if piccmd =="VIW":
			listcmd.append(piccmd)
			print("1'2'3'4'5'6'7'8'9'10")
			print("2*    ______    *   ")
			print("3    /------|  ___*_")
			print("4   /-------| /-----")
			print("5__/--------|/------")
			return self.remoterover()
		else:
			return self.remoterover()
	def viewlog(self):
		print("The history of commands: ")
		print(listcmd)
		return self.remoterover()

class Objects ():
	def __init__(self,name,weight, description):
		self.name = name
		self.weight = weight
		self.description = description
	def __str__(self):
		return "\n*** The Object Information: ***\n- Name: "+ self.name+"\n- Weight: "+ str(self.weight)+"Kg"+"\n- Description: "+self.description+"\n"
	def getname(self):
		return self.name
	def getweight(self):
		return self.weight
	def getdescription(self):
		return self.description
		
class Rock (Objects):
	def __init__(self, color, nature, position, ingredient, name, weight, description):
		self.color = color
		self.nature = nature
		self.position = position
		self.ingredient = ingredient
		super (Rock,self).__init__(name,weight, description)		
	def __str__(self):
		return super(Rock,self).__str__()+"\n- Color: "+ self.color +"\n- Nature: "+ self.nature +"\n- Position: "+ str(self.position)+"\n- Ingredient: "+str(self.ingredient)
	def getcolor(self):
		return self.color			
	def getnature(self):
		return self.nature
	def getposition(self):
		return self.position
	def getingredient(self):
		return self.ingredient

kali = Rovermars("Thissnath","2019-17Eco",[0,0],100, 0, [],100,10, 5)
org = Objects("Duste",3,"it's small rock")
i = Rock("Black","Rock",[0,0],{"H2O":0,"Fr":60},"Asteroid",14,"it's sky rock'")
kali.remoterover()







