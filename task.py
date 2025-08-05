# *****************************TASK ONE************************
age = int(input("Enter your age: "))

if age >= 18 :
    print("You can buy ticket")
    if age >= 60 :
        print("Senior Discount")
else:
    if age >= 12 and age < 18:
        print("Teen Ticket")
    else:
        print("kids ticket")

# ************************TASK TWO****************************

budget = float(input("Enter your budget: "))

if budget >= 500:
	if budget >= 1000:
		print("Google pixel 9pro")
	else:
		print("Iphone")
else:
	if budget < 500:
		if budget == 200:
			print("redmi")
		else:
			print("safe more")
