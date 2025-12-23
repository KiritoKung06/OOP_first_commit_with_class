class Car:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

    def drive(self):
        print(f'{self.brand} , {self.model} is driving')

    my_car =Car('Toyota', 'Vios')
    my_car.drive
       