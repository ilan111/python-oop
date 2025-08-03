from enum import Enum, auto

class Menu(Enum):
    SAVE_A_NEW_ENTRY = auto()
    SEARCH_BY_ID = auto()
    PRINT_AGES_AVERAGE = auto()
    PRINT_ALL_NAMES = auto()
    PRINT_ALL_IDS = auto()
    PRINT_ALL_ENTRIES = auto()
    PRINT_ENTRY_BY_INDEX = auto()
    SAVE_TO_CSV = auto()
    EXIT = auto()

def printMenu():
    for option in Menu:
        print(f"{option.value}. {option.name.replace('_', ' ').title()}")
    
