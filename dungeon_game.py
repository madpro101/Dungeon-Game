import random
# To do 30 January 2020(Nhasi)

# Draw Grid 
# Pick Random Location for player
# Pick Random Location for exit door
# Pick Random Location for monster
# Draw player in the Grid
# take input for movement 
# move player unless invalid move(past edges of grid)
# check for if player won or lost
# clear screen and redraw grid  


CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), 
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), 
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), 
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), 
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
         (0, 5), (1, 5), (2, 5), (3, 5), (4, 5)
         ]

# Function to get the locations 
def get_location():
     monster = None
     door = None
     player = None
    
return monster, player, door
     
while True:
     print("Welcome to the Dungeon. A game proudly made by Dveelopers for Developers")
     print("You are currently in room {}") #fill in position where player is in 
     print("You can move {}") # fill with available moves
     print("Enter QUIT to quit game")
     
     move = input("> " ).upper()
     
     if move == "QUIT":
          break
     
     # Good move? Change player position
     # Bad move? Do not change player position
     # On the door? They win 
     
     
