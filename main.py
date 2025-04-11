from vehicle import Vehicle

class SchoolBus(Vehicle):
    def __init__(self, make, model, capacity):
        super().__init__(make, model)
        self.__capacity = capacity  # encapsulated

    def describe(self):
        return f"This is a school bus that can carry {self.__capacity} students."

    def get_capacity(self):
        return self.__capacity

    def set_capacity(self, capacity):
        self.__capacity = capacity

    def __str__(self):
        return f"SchoolBus: {super().__str__()} with capacity {self.__capacity}"


# Demo
bus = SchoolBus("Ford", "E450", 40)

# Output
print(bus.describe())
print(bus)
print("Make:", bus.make)
print("Model:", bus.model)
print("General Info:", Vehicle.general_info())
print("Vehicle Type:", bus.vehicle_type())
print("Is instance of Vehicle?", isinstance(bus, Vehicle))
