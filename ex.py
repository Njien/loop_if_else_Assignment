
#************************TASK ONE**************************
score = float(input("Enter your score: "))

if score >= 70 and score <= 100:
	print("A")
elif score >=50 and score < 70:
	print("B")
elif score >= 40 and score < 60:
	print("C")
elif score >= 30 and score < 50:
	print("D")
elif score >= 0 and score < 30:
	print("F")
else:
	print("Invalid range")





#*******************TASK TWO***********************

customer = {
		"name": "Godiya",
		"order_amount": 25000,
		"loyalty_card": True,
		"is_student": False
		}

discount_percentage = 0
loyalty = customer["loyalty_card"]

if loyalty:
	discount_percentage += 10
if customer["order_amount"] > 20_000:
	if loyalty:
		discount_percentage += 5
	else:
		print("free soft drink")
if customer["is_student"]:
	discount_percentage += 5

discount = (discount_percentage / 100) * customer["order_amount"]
customer.update({
	"dicount": discount,
	"discount percentage": discount_percentage,
	"amount to pay": customer["order_amount"] - discount
	})
customer_summary ={"customer1": customer}

print(f"discount percentage: {discount_percentage}")
print(f"\ndiscount: {discount}")
print(f"\nsummary of customers: {customer_summary}")
print(f"\ncustomer: {customer}")
