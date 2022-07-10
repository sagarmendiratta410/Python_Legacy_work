
print("Welcome to Love score")

name1 = input("Enter your name")
name2 = input("Enter your partner name")

combined_name = name1 + name2
combined_name_lower = combined_name.lower()

calc_true = combined_name_lower.count('t') + combined_name_lower.count('r') + combined_name_lower.count('u') + combined_name_lower.count('e')
print(calc_true)
calc_love = combined_name_lower.count('l') + combined_name_lower.count('o') + combined_name_lower.count('v') + combined_name_lower.count('e')
print(calc_love)
your_love_score = str(calc_true) + str(calc_love)
print(your_love_score)
check = int(your_love_score)


if (check <10) or (check> 90):
    print("Not good relationship")
elif (check >=40) and (check <=50):
    print("OK relationship")
else:
    print("Your are not in relationship")            