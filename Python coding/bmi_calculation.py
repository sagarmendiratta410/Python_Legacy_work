print("Welcome to BMI Calculator")

height = float(input("Enter your height"))
weight = float(input("Enter your height"))

bmi = weight / height ** 2
print(bmi)
print(type(bmi))

if bmi <= 18.5:
    print("You are underweight")
elif bmi < 25:
    print("You are normal in weight")
elif bmi < 35:
    print("You are obese")
else:
    print("You are clinally obese")                