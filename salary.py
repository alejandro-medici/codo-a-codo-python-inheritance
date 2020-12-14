from empleado import Empleado

class SalaryEmployee(Empleado):
    def __init__(self, name, id):
        super().__init__(name, id)

    def calculate_payroll(self):
        """
        docstring
        """
        return 2000