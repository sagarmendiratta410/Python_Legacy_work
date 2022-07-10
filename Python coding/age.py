current_age = input("what is your current age")

total_age = 90

remaining_life = 90 -int(current_age)
remaining_life_in_days = remaining_life * 365
remaining_life_in_weeks = remaining_life * 52
remaining_life_in_months = remaining_life * 12

print(f" You have {remaining_life_in_days} days, {remaining_life_in_weeks} weeks and {remaining_life_in_months} months left")

result = "You have {0} days, {1} weeks and {2} months left"

print(result.format(remaining_life_in_days ,remaining_life_in_weeks ,remaining_life_in_months))
