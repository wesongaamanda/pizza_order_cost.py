# ============================================================
# Program: Pizza Order Cost Calculator
# Description: Calculates the total cost of a pizza order
#              based on size, toppings, and delivery distance.
# ============================================================

# --- Step 1: Gather User Input ---

# Ask the user for the pizza size (small or large)
size = input("Enter pizza size (small/large): ").strip().lower()

# Ask the user for the number of extra toppings
num_toppings = int(input("Enter the number of additional toppings: "))

# Ask the user for the delivery distance in miles
distance = float(input("Enter delivery distance in miles: "))

# --- Step 2: Calculate Base Pizza Cost ---

# Use if-elif to set the base price based on pizza size
if size == "small":
    base_cost = 8.00   # Small pizza costs $8
elif size == "large":
    base_cost = 12.00  # Large pizza costs $12
else:
    # Handle invalid size input gracefully
    print("Invalid size entered. Please enter 'small' or 'large'.")
    exit()

# --- Step 3: Calculate Topping Cost ---

# Each additional topping costs $1
topping_cost = num_toppings * 1.00

# --- Step 4: Calculate Delivery Fee ---

# $2 for the first 5 miles, $1 per mile beyond that
if distance <= 5:
    delivery_fee = 2.00                          # Flat $2 for up to 5 miles
else:
    delivery_fee = 2.00 + (distance - 5) * 1.00  # $2 + $1 per extra mile

# Pickup orders (0 miles) have no delivery fee
if distance == 0:
    delivery_fee = 0.00

# --- Step 5: Calculate Total Cost ---

# Sum all cost components
total_cost = base_cost + topping_cost + delivery_fee

# --- Step 6: Display the Result ---

# Use an f-string to print a formatted order summary
print(f"\n===== Pizza Order Summary =====")
print(f"Pizza size   : {size.capitalize()}")
print(f"Base cost    : ${base_cost:.2f}")
print(f"Toppings ({num_toppings}): ${topping_cost:.2f}")
print(f"Delivery fee : ${delivery_fee:.2f}")
print(f"-------------------------------")
print(f"Total cost   : ${total_cost:.2f}")
print(f"===============================")