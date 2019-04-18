class Superhedgehog():
    #
    def __init__(self, name,labyrinth):
        self.name = name
        self.labyrinth = labyrinth

    def __str__(self):
        return "The cute hedgehog called: "+ self.name + " now it's in the postion:"+ str(self.start_position()) +" and it must find the way to the finish position in:"+str(self.finish_position())

    def start_position (self):
        #
        for row in self.labyrinth:
            for item in row:
                if item == "S":
                    spx=row.index(item)
                    spy=labyrinth.index(row)
                    startpos=[spx,spy]
        return startpos

    def finish_position (self):
        #
        for row in self.labyrinth:
            for item in row:
                if item == "F":
                    fpx=row.index(item)
                    fpy=labyrinth.index(row)
                    finishpos=[fpx,fpy]
        return finishpos

    def findway(self):
        #
        rock=[]
        road=[]
        for row in self.labyrinth:
            for item in row:
                if item == "R":
                    print("it's a rock")
                elif item == "W":
                    road.append(row.index(item))
                    road.append(labyrinth.index(row))
                    print(road)
    

    def current_position(self,moves):
        #
        for move in moves:
            if move == "up":
                cpx=((self.start_position())[0])
                cpy=((self.start_position())[1])-1
                currentpos=[cpx,cpy]
                return currentpos
            elif move=="down":
                cpx=((self.start_position())[0])
                cpy=((self.start_position())[1])+1
                currentpos=[cpx,cpy]
                return currentpos
            elif move=="right":
                cpx=((self.start_position())[0])+1
                cpy=((self.start_position())[1])
                currentpos=[cpx,cpy]
                return currentpos
            elif move=="left":
                cpx=((self.start_position())[0])-1
                cpy=((self.start_position())[1])
                currentpos=[cpx,cpy]
                return currentpos
            else:
                return self.start_position()

labyrinth=[
    ["R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R"],
    ["S","W","W","W","W","R","W","R","W","R","W","W","W","R","W","R"],
    ["R","R","R","R","W","R","W","W","W","R","W","R","W","R","W","F"],
    ["R","W","W","W","W","R","R","R","W","W","W","R","W","R","W","R"],
    ["R","R","W","R","R","R","W","W","W","R","W","R","W","W","W","R"],
    ["R","W","W","R","R","W","W","R","W","R","W","R","R","W","R","R"],
    ["R","R","W","W","W","W","R","R","W","R","W","W","R","W","W","R"],
    ["R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R"]
]
moves=("up","down","left","right")

h=Superhedgehog("Mimo",labyrinth)
print(h)
hedgehogstart=h.start_position()
print("the start postion: ",hedgehogstart)
hedgehogfinish=h.finish_position()
print("the finish postion: ",hedgehogfinish)
hedgehogmoves=h.current_position(moves)
print("the current postion:",hedgehogmoves)
h.findway()
print(h)