def display_list():
    with open("myfile.txt","r") as file:
        print("student list\n",file.read())

display_list()
        
