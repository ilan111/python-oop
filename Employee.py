from Person import Person

class Employee(Person):
    def __init__(self, id, name, age, field_of_work, salary):
        super().__init__(id, name, age)
        self._field_of_work = field_of_work
        self._salary = salary

    def getFieldOfWork(self):
        return self._field_of_work
    
    def getSalary(self):
        return self._salary
    
    def printEmployee(self):
        return self.printPerson() + f"The field of work is {self.getFieldOfWork()}, the salary is {str(self.getSalary())}"

    def printMyself(self):
        print(self.printEmployee())

    def getCsvLine(self):
        output = super().getCsvLine()
        output["field_of_work"] = self.getFieldOfWork()
        output["salary"] = self.getSalary()
        return output

    
## TESTS FOR MODULE ##
if __name__ == "__main__":
    test_id = 1234
    test_name = "test_name"
    test_age = 20
    test_field_of_work = "Software Engineer"
    test_salary = 2

    employee = Employee(test_id, test_name, test_age, test_field_of_work, test_salary)
    if employee.getID() != test_id:
        print(f"Error: ID should be {str(test_id)} but i got {str(employee.getID())}")

    if employee.getName() != test_name:
        print(f"Error: Name should be {test_name} but i got {employee.getName()}")

    if employee.getAge() != test_age:
        print(f"Error: Age should be {str(test_age)} but i got {str(employee.getAge())}")

    if employee.getFieldOfWork() != test_field_of_work:
        print(f"Error: Field of study should be {test_field_of_work} but i got {employee.getFieldOfWork()}")

    if employee.getSalary() != test_salary:
        print(f"Error: Salary of study should be {test_salary} but i got {employee.getSalary()}")