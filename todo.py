tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Search Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task_name = input("Enter task: ")

        task = {
            "id": len(tasks) + 1,
            "task": task_name
        }

        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for task in tasks:
                print(f"{task['id']}. {task['task']}")

    elif choice == "3":
        keyword = input("Enter task to search: ")

        found = False
        for task in tasks:
            if keyword.lower() in task["task"].lower():
                print(f"Found: {task['id']}. {task['task']}")
                found = True

        if not found:
            print("Task not found.")

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")