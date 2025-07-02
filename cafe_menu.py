print("Welcome to Elssie's Cafe! ☕")
print("Here's our menu:")
menu = {
    "Coffee": 3.00,
    "Tea": 2.00,
    "Sandwich": 6.00,
    "Cake": 4.50
}

for item, price in menu.items():
    print(f"{item}: ${price:.2f}")

order = input("\nWhat would you like to order? ").title()

if order in menu:
    print(f"Great choice! That'll be ${menu[order]:.2f}")
else:
    print("Sorry, we don't have that item.")

order_list = []
total = 0

while True:
    order = input("Enter item to order (or 'done' to finish): ").title()
    if order == "Done":
        break
    if order in menu:
        order_list.append(order)
        total += menu[order]
        print(f"Added {order}. Total so far: ${total:.2f}")
    else:
        print("Sorry, that item is not on the menu.")

print("\nYour Order:")
for item in order_list:
    print(f"- {item}: ${menu[item]:.2f}")
print(f"Total: ${total:.2f}")
