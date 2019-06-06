class Hedgehog():
    #
    def __init__(self, name,labyrinth):
        self.name = name
        self.labyrinth = labyrinth

    def __str__(self):
        return "The cute hedgehog called: "+ self.name + " now it's in the postion:"+ str(self.start_position())

    def start_position (self):
        #
        for row in self.labyrinth: #y pos
            for col in row: #x pos
                if col == "S":
                    spx=row.index(col)
                    spy=self.labyrinth.index(row)
                    startposition = [spx,spy]
                    return startposition

    def finish_position (self):
        #
        for row in self.labyrinth: #y pos
            for col in row: #x pos
                if col == "F":
                    fpx=row.index(col)
                    fpy=self.labyrinth.index(row)
                    finishposition = [fpx,fpy]
                    return finishposition
    
    def findway (self,grid):
        loc = []
        for row in grid:
            for case in row:
                if case == "W":
                    n=(grid.index(row),row.index(case))
                    if n in loc:
                        print ("loc liste",loc)
                    else:
                        loc.append(n)
                        print ("loc liste",loc)
                        print("n",n)

        