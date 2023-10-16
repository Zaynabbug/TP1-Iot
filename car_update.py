class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0

    def start(self):
        print(f"The {self.year} {self.make} {self.model} is starting.")

    def accelerate(self, speed_increase):
        self.speed += speed_increase
        print(f"The car is now moving at {self.speed} mph.")

    def brake(self, speed_decrease):
        if self.speed >= speed_decrease:
            self.speed -= speed_decrease
        else:
            self.speed = 0
        print(f"The car is now moving at {self.speed} mph after braking.")

    def car_info(self):
        print(f"Car Info: {self.year} {self.make} {self.model}, Color: {self.color}, Speed: {self.speed} mph")

# Example usage of the Car class
my_car = Car("Toyota", "Camry", 2022, "Silver")
my_car.start()
my_car.accelerate(30)
my_car.brake(10)
my_car.car_info()  # Display car information
