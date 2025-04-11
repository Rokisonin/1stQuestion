from abc import ABC, abstractmethod

# Abstract base class to define a blueprint for all vehicle types
class Vehicle(ABC):
    def __init__(self, make, model):
        # Encapsulated protected attributes for make and model
        self._make = make
        self._model = model

    # Read-only property to access the make
    @property
    def make(self):
        return self._make

    # Read-only property to access the model
    @property
    def model(self):
        return self._model

    # Abstract method must be implemented by subclasses
    @abstractmethod
    def describe(self):
        pass

    # Static method to provide general info about vehicles
    @staticmethod
    def general_info():
        return "Vehicles are used for transportation."

    # Class method to return the class name of the vehicle
    @classmethod
    def vehicle_type(cls):
        return cls.__name__

    # Dunder method to give a clean string representation of the vehicle
    def __str__(self):
        return f"{self.make} {self.model}"
