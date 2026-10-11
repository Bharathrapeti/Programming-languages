import os
if os.path.exists("example.txt"):
    print("File exists")
else:
    print("File does not exist")




with open("main.txt","r") as file:
    print(file.tell())  
    file.read(5)
    print(file.tell())  


with open("main.txt", "r") as file:
    file.seek(7)  
    print(file.tell())




    with open("matin.txt", "w+") as file:
       file.write("Hello, Python!")
    
       file.seek(0)  
       print(file.tell())  
    
       file.read(6)  
       print(file.tell()) 
    
       file.read(7)  
       print(file.tell())  

