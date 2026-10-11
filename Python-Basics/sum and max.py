def simple_sum(data):
    total = 0
    for item in data:
        print(f"Type of item '{item}':",type(item))
        if isinstance(item,(int,float)):
            total+= item
        else:
            print(f"skipping non-numeric item:{item}")
            return total
def simple_max(data):
    maximum = None
    for item in data:
        print(f"Type of item '{item}':",type(item))
        if isinstance(item,(int,float)):
            if maximum is None or item > maximum:
                maximum = item
        else:
            print(f"skipping non-numeric item:{item}")
    return maximum
data_items = [10,25.5,"hello",3,True,45,"world",2.7]


print("\n---sum function---")
total = simple_sum(data_items)
print("calculated sum:",total)
print("\n---max function---")
max_value = simple_max(data_items)
print("calculated max:",max_value)
                                                 
