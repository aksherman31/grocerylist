#Anabel Sherman
#ToDoList

#Functions
grocery = ["Milk", "Eggs", "Cereal", "Butter"]
doneList = []
def tdProgram():
    global grocery
    choice = int(input("""What would you like to do? Please enter the number of the option you want to select 
    1. View List 
    2. Add to list 
    3. Mark task as completed 
    4. Remove tast from list 
    5. Remove all tasks from the to-do list 
    6. Sort the list alphabetically 
    7. Print the number of Items on the To-do List 
    8. Exit 
    Option: """))
    if choice == 1 :
        print(grocery + doneList)
        tdProgram()
    elif choice == 2 :
        addition = input("What item would you like to add?: ")
        grocery.append(addition)
        tdProgram()
    elif choice == 3 :
        mark = input("What item would you like to mark off?: ")
        doneList.append("X"+mark+"X")
        grocery.remove(mark)
        tdProgram()
    elif choice == 4 :
        remove = input("What would you like to remove from your list?: ")
        grocery.remove(remove)
        tdProgram()
    elif choice == 5 :
        grocery.clear()
        tdProgram()
    elif choice == 6:
        grocery.sort()
        doneList.sort()
        tdProgram()
    elif choice == 7:
        amount = str(len(grocery))
        print("You have "+ amount +" of times on your list")
        tdProgram
    elif choice == 8:
        exit()
    else:
        print("Input did not correspond to one of the options. Please try again: ")
        tdProgram()

#Main
print("Welcome to your personalized grocery list! ")
tdProgram()