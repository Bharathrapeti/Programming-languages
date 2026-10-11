items = []
def add_item():
    name = input("enter the name of the item:")
    item_price = input("enter the price of the item:")
    item_availibility = input("availibility of item?(yes/no):")

    try:
        price = float(item_price)
    except ValueError:
        print("invalid input")
        return
    if item_availibility.lower()in ['yes' ,'y','true','1']:
        availibility = True
    elif item_availibility.lower() in ['no','n','false','0']:
        availibility = False
    else:
        print("invalid thing")
        return
    if isinstance(name,str) and isinstance(price,float) and isinstance(availibility,bool):
        item = {
            "name" : name,
            "price" : price,
            "availibility" : availibility }
        items.append(item)
        print("items added successfully ")
    else:
        print("invalid order")
def show_items():
    if not items:
        print("items are not recorded.\n")
        return
    print("\n---supermarket items---")
    for i, item in enumerate(items,1):
        print(f"{i}.{item['name']} - ${item['price']} - Available:{item['availibility']}")
    print()

while True:
    print("1.add new items")
    print("2.show all elements")
    print("3.exit")
    choice = input("choice select (1-3):")
    if choice == '1':
      add_item()
    elif choice == '2':
      show_items()
    elif choice == '3':
      print("good bye")
    else:
      print("invalid choice.try again")
    
