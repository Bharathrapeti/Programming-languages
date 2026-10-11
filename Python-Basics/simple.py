def creating_file():
    with open("sample.txt", "w") as file:
        file.write("Hello, World!")   
    print("File created and data written successfully!")

def display_file():
    with open("sample.txt", "r") as file:
        print("File Content:", file.read())

creating_file()  
display_file()  
