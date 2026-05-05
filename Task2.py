# Simple To-Do List 

print("Welcome to the To-Do List!")
print("")

# Create an empty list to store tasks
tasks = []

# Main loop - keeps running until user chooses to exit
while True:
    print("Please select an option:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # Option 1: Add a task
    if choice == "1":
        task = input("Enter the task you want to add: ")
        tasks.append(task)
        print("Task '" + task + "' added to the list.")
        print("")

    # Option 2: View all tasks
    elif choice == "2":
        if len(tasks) > 0:  # Check if list is not empty
            print("Your To-Do List:")
            for i in range(len(tasks)):
                print(str(i+1) + ". " + tasks[i])
        else:
            print("Your To-Do List is empty.")
        print("")

    # Option 3: Remove a task
    elif choice == "3":
        if len(tasks) > 0:
            print("Your To-Do List:")
            for i in range(len(tasks)):
                print(str(i+1) + ". " + tasks[i])

            task_num = input("Enter the number of the task you want to remove: ")

            # Convert input to number and check if valid
            if task_num.isdigit():  # Check if input is a number
                task_num = int(task_num)
                if task_num >= 1 and task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print("Task '" + removed_task + "' removed from the list.")
                else:
                    print("Invalid task number. Please enter a number between 1 and " + str(len(tasks)))
            else:
                print("Please enter a valid number.")
        else:
            print("Your To-Do List is empty. Nothing to remove.")
        print("")

    # Option 4: Exit the program
    elif choice == "4":
        print("Thank you for using the To-Do List. Goodbye!")
        break

    # Invalid choice
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
        print("")



            
        