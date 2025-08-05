from Employee import Employee
from Person import Person
from Student import Student
from Menu import Menu, printMenu
import pandas as pd

############# FUNCTIONS #############


# CHECK INPUTS
def isNumber(input: str, type: str):
    if not input.isdigit():
        print(f"Error: {type} must be a number. {input} is not a number")
        return False
    
    return True

def isValidAge(input: str):
    if not isNumber(input, "age"):
        return False
    
    elif int(input) > 120 or int(input) < 0:
        print(f"Error: Age must be a number between 0 to 120")
        return False
    
    return True

def isValidMenuChoice(input: str, min_value: int, max_value: int):
    if not input.isdigit():
        print(f"Error: you must enter a number between {min_value} to {max_value}")
        return False
        
    elif input.isdigit() and (int(input) < min_value or int(input) > max_value):
        print(f"Error: Option [{input}] does not exist. Please try again")
        return False
        
    return True

# OPTION 1
def saveNewEntry(data: dict, count: dict, ids: list):
    person_type = input(choosePersonTypeStr())
    while not isValidMenuChoice(person_type, 1, 3):
        person_type = input(choosePersonTypeStr())

    id = input("ID: ")
    if not isNumber(id, "ID"):
        return
    
    id = int(id)
    if id in data:
        print(f"Error: ID already exists: {data[id]}")
        return

    name = input("Name: ")
    age = input("Age: ")
    if not isValidAge(age):
        return
    
    age = int(age)

    if person_type == "1":
        new_person = Person(id=id, name=name, age=age)
        data[id] = new_person
    
    elif person_type == "2":
        field_of_study = input("Field of study: ")
        year_of_study = input("Year of study: ")
        if not isNumber(year_of_study, "Year of study"):
            return
        year_of_study = int(year_of_study)
        score_avg = input("Score Average: ")
        if not isNumber(score_avg, "Score Average"):
            return
        score_avg = int(score_avg)
        new_student = Student(id=id, name=name, age=age, field_of_study=field_of_study, year_of_study=year_of_study, score_avg=score_avg)
        data[id] = new_student

    elif person_type == "3":
        field_of_work = input("Field of work: ")
        salary = input("Salary: ")
        if not isNumber(salary, "Salary"):
            return
        salary = int(salary)
        new_employee = Employee(id=id, name=name, age=age, field_of_work=field_of_work, salary=salary)
        data[id] = new_employee
        

    # if id in data:
    print(f"ID [{id}] saved successfully")
    count["ages_sum"] += age
    count["id_count"] += 1
    ids.append(id)


# OPTION 2
def searchById(data: dict):
    id = input("Please enter the ID you want to look for: ")
    if not isNumber(id, "id"):
        return
    
    id = int(id)

    if id in data.keys():
        data[id].printPerson()

    else:
        print(f"Error: ID {id} is not saved")

# OPTION 3
def printAgesAverage(count: dict):
    if count["id_count"] > 0:
        average_age = count["ages_sum"] / count["id_count"]
        print(f"Average age is: {average_age}")
    
    else:
        print("Error: Can't divide by 0")
    
# OPTION 4
def printAllNames(data: dict):
    for i, entry in enumerate(data.values()):
        print(f"{i}. {entry.getName()}")

# OPTION 5
def printAllIds(data: dict):
    for i, entry in enumerate(data.values()):
        print(f"{i}. {entry.getID()}")

# OPTION 6
def printAllEntries(data: dict):
    for i, entry in enumerate(data.values()):
        print(f"{i}.", end=" ")
        entry.printMyself()

# OPTION 7
def printEntryByIndex(data: dict, ids: list):
    user_input = input("Please enter the index you want to print: ")
    if not isNumber(user_input, "index"):
        return
    
    index = int(user_input)
    # data_list = list(data.items())

    if index < len(ids):
        id = ids[index]
        data[id].printMyself()

    else:
        print(f"Error: Index out of range. The maxium index allowd is {len(ids)-1}")

# OPTION 8    
def saveToCSV(data: dict):
    output_file_name = input("What is your output file name? ").strip() + ".csv" or "output.csv"
    data_table = [obj.getCsvLine() for obj in data.values()]
    df = pd.DataFrame(data_table)
    df.to_csv(output_file_name, index=False)

# OPTION 9
def exitProgram():
    try:
        while True:
            user_input = input("Are you sure? (y/n) ")
            if user_input == "y":
                print("Goodbye!")
                exit()

            elif user_input == "n":
                return
            
    except KeyboardInterrupt:
        print("Goodbye!")
        exit()

# ETC
def choosePersonTypeStr():
    return "Choose person type:\n1 - Regular person\n2 - Student\n3 - Employee\n"

def handleMenuOption(choice: Menu, data: dict, counter: dict, id_list: list):
    if choice == Menu.SAVE_A_NEW_ENTRY:
        saveNewEntry(data, counter, id_list)

    elif choice == Menu.SEARCH_BY_ID:
        searchById(data)

    elif choice == Menu.PRINT_AGES_AVERAGE:
        printAgesAverage(counter)

    elif choice == Menu.PRINT_ALL_NAMES:
        printAllNames(data)

    elif choice == Menu.PRINT_ALL_IDS:
        printAllIds(data)

    elif choice == Menu.PRINT_ALL_ENTRIES:
        printAllEntries(data)

    elif choice == Menu.PRINT_ENTRY_BY_INDEX:
        printEntryByIndex(data, id_list)

    elif choice == Menu.SAVE_TO_CSV:
        saveToCSV(data)

    elif choice == Menu.EXIT:
        exitProgram()

############# MAIN #############

def main():
    data = {}
    counter = {"ages_sum": 0, "id_count": 0}
    id_list = []
    demo_data = {10: Person(10, "Dave", 24), 
                20: Student(20, "Nate", 31, "Software Engineering", 2, 90),
                30: Employee(30, "Bob", 43, "Cleaner", 10000)}

    while True:
        printMenu()
        try:
            user_choice = int(input("Please enter your choice: "))
            selected_option = Menu(user_choice)
            handleMenuOption(choice=selected_option, data=demo_data, counter=counter, id_list=id_list)

        except ValueError:
            print("Please enter a valid option (1-9)")

        except KeyError:
            print("Invalid option. Please try again")

        except KeyboardInterrupt:
            print("Goodbye!")
            exitProgram()

        except Exception as e:
            print(f"Unexpected error: {e}")
        
        input("Press to continue")
        
if __name__ == "__main__":
    main()