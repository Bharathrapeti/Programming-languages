# Supermarket Inventory System Without Try-Except

def get_item_details():
    # Input: Item name
    item_name = input("Enter item name: ")
    print(f"Type of item_name: {type(item_name)}")  # Should be str

    # Input: Item price with type validation
    item_price_input = input("Enter item price: ")
    if item_price_input.replace('.', '', 1).isdigit():
        item_price = float(item_price_input)
        print(f"Type of item_price: {type(item_price)}")  # Should be float
    else:
        print("Invalid price. It must be a number.")
        return

    # Input: Availability check
    availability_input = input("Is the item available? (yes/no): ").strip().lower()
    if availability_input == "yes":
        item_available = True
    elif availability_input == "no":
        item_available = False
    else:
        print("Invalid availability. Please enter 'yes' or 'no'.")
        return
    print(f"Type of item_available: {type(item_available)}")  # Should be bool

    # Final output
    print("\n--- Item Recorded ---")
    print(f"Name       : {item_name}")
    print(f"Price      : ₹{item_price:.2f}")
    print(f"Available  : {'Yes' if item_available else 'No'}")

    return {"name": item_name, "price": item_price, "available": item_available}

# Run the function
if __name__ == "__main__":
    item = get_item_details()
