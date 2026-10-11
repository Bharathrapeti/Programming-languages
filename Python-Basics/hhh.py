# Supermarket Item Recording System

items = []

def add_item():
    name = input("Enter item name: ")
    price_input = input("Enter item price: ")
    availability_input = input("Is the item available? (yes/no): ")

    # Type conversion
    try:
        price = float(price_input)
    except ValueError:
        print("❌ Invalid price. Must be a number.")
        return

    # Convert availability input to boolean
    if availability_input.lower() in ['yes', 'y', 'true', '1']:
        availability = True
    elif availability_input.lower() in ['no', 'n', 'false', '0']:
        availability = False
    else:
        print("❌ Invalid availability. Use 'yes' or 'no'.")
        return

    # Type checks
    if isinstance(name, str) and isinstance(price, float) and isinstance(availability, bool):
        item = {
            "name": name,
            "price": price,
            "availability": availability
        }
        items.append(item)
        print("✅ Item added successfully!\n")
    else:
        print("❌ Data types are incorrect.")

def show_items():
    if not items:
        print("No items recorded.\n")
        return
    print("\n--- Supermarket Items ---")
    for i, item in enumerate(items, 1):
        print(f"{i}. {item['name']} - ₹{item['price']} - Available: {item['availability']}")
    print()

# Main loop
while True:
    print("1. Add New Item")
    print("2. Show All Items")
    print("3. Exit")
    choice = input("Choose an option (1-3): ")

    if choice == '1':
        add_item()
    elif choice == '2':
        show_items()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")
