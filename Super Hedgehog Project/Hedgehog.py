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

    def current_position(self,startpostion,moves):
        #
        print("The current move:",move)
        if move == "up":
            cpx=(startpostion[0])
            cpy=(startpostion[1])-1
            currentpos=[cpx,cpy]
            print("up")
            return currentpos
        elif move=="down":
            cpx=(startpostion[0])
            cpy=(startpostion[1])+1
            currentpos=[cpx,cpy]
            print("down")
            return currentpos
        elif move=="right":
            cpx=(startpostion[0])+1
            cpy=(startpostion[1])
            currentpos=[cpx,cpy]
            print("right")
            return currentpos
        elif move=="left":
            cpx=(startpostion[0])-1
            cpy=(startpostion[1])
            currentpos=[cpx,cpy]
            print("left")
            return currentpos
        else:
            return startpostion

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

moves=["right","right","right","right","down"]

h=Superhedgehog("Mimo",labyrinth)
print(h)
hedgehogstart=h.start_position()
print("The start postion: ",hedgehogstart)
hedgehogfinish=h.finish_position()
print("The finish postion: ",hedgehogfinish)

if len(moves)!= 0:
    for move in moves:
        hedgehogmoves=h.current_position(hedgehogstart,move)
        print("The current postion:",hedgehogmoves)

print(h)