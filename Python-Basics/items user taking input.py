item = input("enter item name:")
item_price = float(input("enter item price:"))
item_availble = input("item is there or not (yes / not):?")

try:
    price = float(item_price)
    availability = True if item_availble.lower() == "yes" else False
    
    print("name type:",type(item))
    print("Price type:",type(item_price))
    print("item-availble:",type(item_availble))

    if isinstance(item,str)and isinstance(item_price,float) and isinstance(item_availble, bool):
        print(f"\nitem'{item}'recorded with price ₹{item_price:2f}")
        if availability:
            print("item is available for purchase.")
        else:
            print("item is not available for purchase")
    else:
            print("one or more inputs are of the wrong type.")
except ValueError:
    print("price must be a number.")
