pizza_size = input("Enter pizza size (small or large): ").strip().lower()

num_toppings = int(input("Enter the number of additional toppings: "))

delivery_distance = float(input("Enter the delivery distance in miles: "))

if pizza_size == "small":
    base_cost = 8.00   
elif pizza_size == "large":
    base_cost = 12.00  
else:
    
    print("Invalid pizza size entered. Please enter 'small' or 'large'.")
    exit()

toppings_cost = num_toppings * 1.00

if delivery_distance <= 5:
    delivery_fee = 2.00
else:
    extra_miles = delivery_distance - 5
    delivery_fee = 2.00 + (extra_miles * 1.00)

total_cost = base_cost + toppings_cost + delivery_fee


print("\n===== Pizza Order Summary =====")
print(f"Pizza size:      {pizza_size.capitalize()}")
print(f"Base cost:       ${base_cost:.2f}")
print(f"Toppings ({num_toppings}):    ${toppings_cost:.2f}")
print(f"Delivery fee:    ${delivery_fee:.2f}  ({delivery_distance} miles)")
print("--------------------------------")
print(f"Total cost:      ${total_cost:.2f}")
print("================================")



