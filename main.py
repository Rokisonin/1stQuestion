from vehicle import Vehicle

# SchoolBus is a specialized type of Vehicle (Inheritance)
class SchoolBus(Vehicle):
    def __init__(self, make, model, capacity):
        # Initialize base class with make and model
        super().__init__(make, model)
        # Encapsulated capacity attribute (private)
        self.__capacity = capacity

    # Concrete implementation of abstract method from Vehicle
    def describe(self):
        return f"This is a school bus that can carry {self.__capacity} students."

    # Getter method for capacity
    def get_capacity(self):
        return self.__capacity

    # Setter method for capacity
    def set_capacity(self, capacity):
        self.__capacity = capacity

    # Dunder method for human-readable string output
    def __str__(self):
        return f"SchoolBus: {super().__str__()} with capacity {self.__capacity}"


# ---------- Demo Usage ----------
# Create an instance of SchoolBus
bus = SchoolBus("Ford", "E450", 40)

# Call methods and print results
print(bus.describe())                            # Custom describe() implementation
print(bus)                                       # __str__ method output
print("Make:", bus.make)                         # Access protected attribute via property
print("Model:", bus.model)                       # Same as above
print("General Info:", Vehicle.general_info())   # Call static method
print("Vehicle Type:", bus.vehicle_type())       # Call class method
print("Is instance of Vehicle?", isinstance(bus, Vehicle))  # True because SchoolBus inherits Vehicle
