print("welcome to treasure island, letsperform the mision")

move = input("Would you like to move Left or Right, use L or R\n")

if move == "L":
    next_move = input("Would you like to swim or Wait. For Swim use S and to wait use W\n")
    if next_move =="W":
       door = input("Would you like to go to Red door or Yellow or Blue. Use R, B or Y\n")
       if door == "Y":
         print("You won the Game")
       else:
         print("Game over")
    elif next_move == "S":
        print("Game over")
    else:
        print("You opted wrong option")    
elif move == "R":
    print("You Lost the Game")    
else:
    print("You are not playing the game")    
   