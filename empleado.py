from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, name, id, address=None):
        self.name = name
        self.id = id
        self.address = address
    
    @abstractmethod
    def calculate_payroll(self):
        pass