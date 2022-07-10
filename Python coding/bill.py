print("welcome to tip calculator")
initial_bill = input("what is total bill")
percentage_tip = input("what is percentage tip you would like to give ? 10, 12, or 15?")
total_person = input("Total number of peoples available")

print(type(initial_bill))
print(type(percentage_tip))
print(type(total_person))

total_bill = float(initial_bill) + float(initial_bill) * float(percentage_tip) * float(0.01)
print(total_bill)

bill_perperson = float(total_bill) / float(total_person)
print(bill_perperson)