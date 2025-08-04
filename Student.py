from Person import Person

class Student(Person):
    def __init__(self, id, name, age, field_of_study, year_of_study,score_avg):
        super().__init__(id, name, age)
        self._field_of_study = field_of_study
        self._year_of_study = year_of_study
        self._score_avg = score_avg

    def getFieldOfStudy(self):
        return self._field_of_study
    
    def getYearOfStudy(self):
        return self._year_of_study
    
    def getScoreAvg(self):
        return self._score_avg

    def printStudent(self):
        return self.printPerson() + f"The field of study is {self.getFieldOfStudy()}, the year of study is {str(self.getYearOfStudy())}, the avg is {str(self.getScoreAvg())}"

    def printMyself(self):
        print(self.printStudent())

    def getCsvLine(self):
        return {
            "id": super().getID(),
            "type": super().getType(),
            "name": super().getName(),
            "age": super().getAge(),
            "field_of_study" : self.getFieldOfStudy(),
            "year_of_study" : self.getYearOfStudy(),
            "score_avg" : self.getScoreAvg(),
        }

## TESTS FOR MODULE ##
if __name__ == "__main__":
    test_id = 1234
    test_name = "test_name"
    test_age = 20
    test_field_of_study = "Software Engineer"
    test_year_of_study = 2
    test_score_avg = 90

    student = Student(test_id, test_name, test_age, test_field_of_study, test_year_of_study, test_score_avg)
    if student.getID() != test_id:
        print(f"Error: ID should be {str(test_id)} but i got {str(student.getID())}")

    if student.getName() != test_name:
        print(f"Error: Name should be {test_name} but i got {student.getName()}")

    if student.getAge() != test_age:
        print(f"Error: Age should be {str(test_age)} but i got {str(student.getAge())}")

    if student.getFieldOfStudy() != test_field_of_study:
        print(f"Error: Field of study should be {test_field_of_study} but i got {student.getFieldOfStudy()}")

    if student.getYearOfStudy() != test_year_of_study:
        print(f"Error: Year of study should be {test_year_of_study} but i got {student.getYearOfStudy()}")

    if student.getScoreAvg() != test_score_avg:
        print(f"Error: Score avg should be {str(test_score_avg)} but i got {str(student.getScoreAvg())}")