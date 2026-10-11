item_name = input("Enter the item name: ")
item_price = input("Enter the item price: ")
item_available = input("Is the item available? (True/False): ")
# Step 2: Validate and trace the data types
print("\nTracing the data types of inputs:")
print(f"Item Name: {item_name} - Type: {type(item_name)}")
try:
# Convert item_price to float and check type
 item_price = float(item_price)
 print(f"Item Price: {item_price} - Type: {type(item_price)}")
except ValueError:
 print("Error: Item price must be a number (float). Exiting...")
 exit()
try:
# Convert item_available to boolean and check type
 if item_available.lower() == "true":
  item_available = True
 elif item_available.lower() == "false":
  item_available = False
 else:
  raise ValueError
  print(f"Item Availability: {item_available} - Type: {type(item_available)}")
except ValueError:
 print("Error: Item availability must be 'True' or 'False'. Exiting...")
 exit()
# Step 3: If all inputs are valid, display the item details
print("\nItem Details:")
print(f"Name: {item_name}")
print(f"Price: ${item_price:.2f}")
print(f"Available: {'Yes' if item_available else 'No'}")
