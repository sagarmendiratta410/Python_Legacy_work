



# Question is Boy height if greater or qual to than 120 he can join cricket team but if it is less than he cannot.
# And if height is more than 120 then check age. If age is less than 10, pay #5 and if age is less than equal to 20 pay $15 and finally if age is more than 20 Pay $20.


print("Welcome to cricket team boys!!")

height = int(input("Please eneter your height in cm"))
age = int(input("Enter your age"))
bill = 0

if height >= 120:
    print("You are eligible for cricket team")
    if age <= 10:
        bill = 5
        print("You need to pay only $5")
    elif age <= 20:
        bill = 15
        print("You need to pay only $15")    
    elif age > 45 and age <55:
         print("You dont need to pay anything as your senior")    
    else:
        bill = 20
        print("You need to pay only $20")
    want_photo = input("Do you want photos, Y or N?")
    if want_photo == "Y":
        bill = bill + 3
    print(f"Your Total bill is {bill}")
else:
    print("You are not eligible for cricket team")

