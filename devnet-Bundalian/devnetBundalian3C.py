"""
Midterm Practical Exam — Pet Adoption Records Manager
Student: Bundalian, Clarence James L.
"""

pets = []  # starts empty — the user adds pets as the program runs


def display_menu():
    print("=== Pet Adoption Records ===")
    print(" 1. Add a pet")
    print(" 2. View all pets")
    print(" 3. Count available vs adopted")
    print(" 4. Find a pet by name")
    print(" 5. Exit")
    choice = int(input("Choose a option: ")) 
      
    # print the menu, return the user's choice 
    pass

def add_pet(pet_list):
    name = input("Name of the Pet: ")
    animaltype = input("Type of the Pet: ")
    status = input("Status of the Pet: ")

    # ask for name, animal type, status — build the string, add to the list
    pass

def view_pets(pet_list):
    # loop through and print every pet — handle empty list
    pass

def count_available_adopted(pet_list):
    # loop through, count Available vs Adopted, return both
    pass

def find_pet(pet_list):
    # ask for a name, search the list, print result or "not found"
    pass

# BONUS (optional)
def remove_pet(pet_list):
    # your code here
    pass

def main():
    running = True
    while running:
        choice = display_menu()
        # use if/elif to call the right function based on choice
        # set running = False when the user picks Exit
        if choice == 1:
            print(add_pet)
        elif choice == 2:
            print(view_pets)
        elif choice == 3:
            print(count_available_adopted)
        elif choice == 4:
            print(find_pet)
        elif choice == 5:
            print("Thank you Come again!")
        else:
            print("Invalid")

main()
