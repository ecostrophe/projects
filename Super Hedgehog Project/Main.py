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

moves=["right","right","right","right","down"]

h=Hedgehog("Mimo",labyrinth)
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