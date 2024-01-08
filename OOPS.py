class Employee:
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary
    def getSalary(self):
        print(self.salary)

vinay = Employee("Vinay", "10")
print(vinay.name)
print(vinay.salary)
vinay.getSalary()