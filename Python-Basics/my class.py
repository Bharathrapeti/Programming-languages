class laptop:
  def names(self):
     print("it is my lapttop")
     laptop="lenovo"

lap = laptop()
lap.names()




class Laptop:
   def names(self,brand):
       print(f"It is my {brand} laptop.")

# Creating an object of the classLaptop()

# Calling the method
Laptop().names("lenovo")


class Laptop:
    def names(self, brand="Laptop"):
        print(f"It is my {brand}.")

Laptop().names("Lenovo")
