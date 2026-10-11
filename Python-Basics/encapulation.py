class Car:
    def __init__(self):
        self.steering = "Steering Wheel"      
        self.wheels = 4                       
        self.brake = "Brake Pedal"           
        self.accelerator = "Accelerator Pedal"  
        self.__engine_status = "Off"          

    def start_engine(self):
        self.__engine_status = "On"
        print("Engine started.")

    def stop_engine(self):
        self.__engine_status = "Off"
        print("Engine stopped.")

    def show_engine_status(self):
        print("Engine is currently:", self.__engine_status)


my_car = Car()

print("Car has:", my_car.steering)
print("Car has:", my_car.brake)
print("Car has:", my_car.accelerator)
print("Number of wheels:", my_car.wheels)


my_car.start_engine()
my_car.show_engine_status()
my_car.stop_engine()
my_car.show_engine_status()
