tasks = []

while True:

    print("1. Add a task")
    print("2. Remove a task")
    print("3. Display all the tasks")
    print("4. Quit")
    choice = input("Press enter a task: ").strip()



    if choice == "1":
        tasks_to_add = input("Enter the tasks you want to add: ")
        tasks.append(tasks_to_add)
    elif choice == "2":
        tasks_to_remove = input("Enter the tasks you want to remove: ")
        if tasks_to_remove in tasks:
            tasks.remove(tasks_to_remove)
            print("The task has been removed")
        else:
            print("The task does not exist")
    elif choice == "3":
        print(f"Tasks: {tasks}")
        print("---------------------------------------")
    elif choice == "4":
            print("Goodbye!")
            exit()
    else:
            print("Invalid input")




