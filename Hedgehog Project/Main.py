from Hedgehog import *

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
moves=["up","right","right","right","down"]

h=Hedgehog("Mimo",labyrinth)
print(h)
print(h.start_position())
print(h.finish_position())
h.findway(labyrinth)