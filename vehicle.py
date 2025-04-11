from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model):
        self._make = make
        self._model = model

    @property
    def make(self):
        return self._make

    @property
    def model(self):
        return self._model

    @abstractmethod
    def describe(self):
        pass

    @staticmethod
    def general_info():
        return "Vehicles are used for transportation."

    @classmethod
    def vehicle_type(cls):
        return cls.__name__

    def __str__(self):
        return f"{self.make} {self.model}"
