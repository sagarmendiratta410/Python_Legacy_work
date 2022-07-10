print("Welcome to Dominoz Pizza")

size = input("What would like to have Sir/Mam S, M or L pizza\n")
Bill = 0

if size == "S":
    bill =  15   
elif size =="M":
   bill = 20
elif size =="L":
   bill = 25
else:
    print("You are planning to eat next time")    

add_pepperoni = (input("Would you like to add extra pepperoni?  Y or N\n"))
if add_pepperoni == "Y":
    bill = bill + 2
extra_cheeze =  (input("Would you like to add extra cheeze?  Y or N\n"))
if extra_cheeze =="Y":
    bill = bill + 3
print(f"Your total bill is ${bill}")
