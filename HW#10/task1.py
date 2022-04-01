class Vehicle():
    max_speed = 0
    mileage = 0


class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

class Electric(Car):
    pass

class Petrol(Car):
    pass


print(issubclass(Bus, Vehicle))
print(issubclass(Car, Vehicle))

print(issubclass(Electric, Car))
print(issubclass(Petrol, Car))

bus = Bus()
print(isinstance(bus, Vehicle))

car = Car()
print(isinstance(car, Car))
print(isinstance(car, Vehicle))

electric = Electric()
print(isinstance(electric, Car))
print(isinstance(electric, Vehicle))

petrol = Petrol()
print(isinstance(petrol, Car))
print(isinstance(petrol, Vehicle))

