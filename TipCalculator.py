print("Welcome to the Tip Calculator!")
bill = float(input("Kindly enter your bill : $"))
tip = int(input("what percentage do you want to tip the waiter? (10 , 12 0r 15 ): "))
no_of_guests = int(input("How many people are on this table? "))

tip_percentage = tip / 100
total_tip = bill * tip_percentage
total_bill = round((bill + total_tip) / no_of_guests, 2)
print(f"You all will be required to pay: {total_bill} \nCiao!!!!")

