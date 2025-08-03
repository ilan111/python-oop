class Person:
    def __init__(self, id, name, age):
        self._id = id
        self._name = name
        self._age = age

    def setName(self, name):
        self._name = name

    def getID(self):
        return self._id
    
    def getName(self):
        return self._name
    
    def getAge(self):
        return self._age
    
    def getType(self):
        return str(type(self)).split("'")[1].split(".")[0]
    
    def printPerson(self):
        return f"The {self.getType()}\t (ID: {self.getID()})\tName: {self.getName()} is {self.getAge()} years old.\t"

    def printMyself(self):
        print(self.printPerson())

## TESTS FOR MODULE ##
if __name__ == "__main__":
    test_id = 1234
    test_name = "test_name"
    test_age = 20

    person = Person(test_id, test_name, test_age)
    if person.getID() != test_id:
        print(f"Error: ID should be {str(test_id)} but i got {str(person.getID())}")

    if person.getName() != test_name:
        print(f"Error: Name should be {test_name} but i got {person.getName()}")

    if person.getAge() != test_age:
        print(f"Error: Age should be {str(test_age)} but i got {str(person.getAge())}")

    