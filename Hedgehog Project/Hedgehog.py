class Hedgehog():
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
                    spy=self.labyrinth.index(row)
                    startpos=[spx,spy]
        return startpos

    def finish_position (self):
        #
        for row in self.labyrinth:
            for item in row:
                if item == "F":
                    fpx=row.index(item)
                    fpy=self.labyrinth.index(row)
                    finishpos=[fpx,fpy]
        return finishpos

    def findway(self):
        #
        road=[]
        for row in self.labyrinth:
            for item in row:
                if item == "R":
                    print("it's a rock")
                elif item == "W":
                    road.append(row.index(item))
                    #road.append(labyrinth.index(row))
                    print(road)

    def current_position(self,startposition,move):
        #
        xmoveposition= 0
        ymoveposition= 0
        if move == "up":
            ymoveposition-=1
            print("xmoveposition",xmoveposition,"ymoveposition",ymoveposition)
            cpx=(startposition[0])+ xmoveposition
            cpy=(startposition[1])+ymoveposition
            currentpos=[cpx,cpy]
            print("up")
            return currentpos
        elif move=="down":
            ymoveposition+=1
            print("xmoveposition",xmoveposition,"ymoveposition",ymoveposition)
            cpx=(startposition[0])+xmoveposition
            cpy=(startposition[1])+ymoveposition
            currentpos=[cpx,cpy]
            print("down")
            return currentpos
        elif move=="right":
            xmoveposition+=1
            print("xmoveposition",xmoveposition,"ymoveposition",ymoveposition)
            cpx=(startposition[0])+xmoveposition
            cpy=(startposition[1])+ymoveposition
            currentpos=[cpx,cpy]
            print("right")
            return currentpos
        elif move=="left":
            xmoveposition-=1
            print("xmoveposition",xmoveposition,"ymoveposition",ymoveposition)
            cpx=(startposition[0])+xmoveposition
            cpy=(startposition[1])+ymoveposition
            currentpos=[cpx,cpy]
            print("left")
            return currentpos
        else:
            return startposition