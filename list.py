tasks = []

def show_menu():
    print("\n TO-DO LIST APP ")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter a new task: ")
        tasks.append({"task": task, "done": False})
        print("Task added successfully!")

    elif choice == '2':
        print("\nYour Tasks:")
        for i, t in enumerate(tasks):
            status = "✔️" if t["done"] else "❌"
            print(f"{i+1}. {t['task']} [{status}]")

    elif choice == '3':
        num = int(input("Enter task number to mark as done: "))
        if 0 < num <= len(tasks):
            tasks[num-1]["done"] = True
            print("Task marked as done!")

    elif choice == '4':
        num = int(input("Enter task number to delete: "))
        if 0 < num <= len(tasks):
            tasks.pop(num-1)
            print("Task deleted successfully!")

    elif choice == '5':
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
        