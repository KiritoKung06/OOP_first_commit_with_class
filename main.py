class Car:
    def __init__(self, brand, model):
        self.model = model
        self.brand = brand

    def drive(self):
        print(f'{self.brand} , {self.model} is driving')

my_car = Car('Toyota', 'Vios')
my_car.drive

class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def charge(self):
        print(f"{self.battery} Battery is charging...")
    
my_ev = ElectricCar("Tesla", "Model 3", 75) 
my_ev.drive()
my_ev.charge()
