# ============================================================
# Pizza Order Cost Calculator
# Lab: Python Programming
# Description: Calculates the total cost of a pizza order
#              based on size, toppings, and delivery distance.
# ============================================================


# ---- Step 1: Gather User Input ----

# Ask the user for the pizza size (small or large)
pizza_size = input("Enter pizza size (small or large): ").strip().lower()

# Ask the user for the number of additional toppings
num_toppings = int(input("Enter the number of additional toppings: "))

# Ask the user for the delivery distance in miles
delivery_distance = float(input("Enter the delivery distance in miles: "))


# ---- Step 2: Calculate Base Pizza Cost ----

# Use conditional statements to set the base price based on size
if pizza_size == "small":
    base_cost = 8.00   # Small pizza costs $8
elif pizza_size == "large":
    base_cost = 12.00  # Large pizza costs $12
else:
    # Handle invalid size input
    print("Invalid pizza size entered. Please enter 'small' or 'large'.")
    exit()


# ---- Step 3: Calculate Toppings Cost ----

# Each additional topping costs $1
toppings_cost = num_toppings * 1.00


# ---- Step 4: Calculate Delivery Fee ----

if delivery_distance <= 5:
    # $2 flat fee for the first 5 miles
    delivery_fee = 2.00
else:
    # $2 for the first 5 miles + $1 for each mile beyond 5
    extra_miles = delivery_distance - 5
    delivery_fee = 2.00 + (extra_miles * 1.00)


# ---- Step 5: Calculate Total Cost ----

# Sum all cost components
total_cost = base_cost + toppings_cost + delivery_fee


# ---- Step 6: Display the Result ----

# Use an f-string to display a formatted cost breakdown
print("\n===== Pizza Order Summary =====")
print(f"Pizza size:      {pizza_size.capitalize()}")
print(f"Base cost:       ${base_cost:.2f}")
print(f"Toppings ({num_toppings}):    ${toppings_cost:.2f}")
print(f"Delivery fee:    ${delivery_fee:.2f}  ({delivery_distance} miles)")
print("--------------------------------")
print(f"Total cost:      ${total_cost:.2f}")
print("================================")