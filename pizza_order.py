# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

pizza_price = 0
pepperoni_price = 0
extra_cheese_for_any_size_pizza = 0

if size == "S":
    pizza_price = 15
    if add_pepperoni == "Y":
        pepperoni_price = 2
        pizza_price += 2
        
elif size == "M":
    pizza_price = 20
    if add_pepperoni == "Y":
        pepperoni_price = 3
        pizza_price += 3
        
elif size == "L":
    pizza_price = 25
    if add_pepperoni == "Y":
        pepperoni_price = 3
        pizza_price += 3
        
if extra_cheese == "Y":
    extra_cheese_for_any_size_pizza = 1
    pizza_price += 1
    
print(f"Your final bill is: ${pizza_price}")

