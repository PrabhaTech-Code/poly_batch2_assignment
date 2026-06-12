#Class Definition rules
 #1. Class name should start with a capital letter.
    #2. Class name should be a noun.
#Method Definition rules
 #1. Method name should start with a lowercase letter.
    #2. Method name should be a verb.

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Vehicle Make: {self.make}, Model: {self.model}")

# v = Vehicle("Toyota", "Camry")
# v.display_info()

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)  # Call the constructor of the parent class
        self.num_doors = num_doors

    def display_car_info(self):
        print(f"Number of Doors: {self.num_doors}")


c = Car("Honda", "Civic", 4)
c.display_info()
c.display_car_info()    
