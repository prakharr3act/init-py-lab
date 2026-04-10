# Exercise 2 Shopping Cart Program

item = input("Enter the item you want to purchase: ")
quantity = int(input("Enter the quantity: "))
price = float(input("Enter the price of the item: "))
total_Cost = quantity * price
print(f"The total cost of your purchase is: ${total_Cost:.2f}")