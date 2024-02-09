#to do list manager
tasks = []

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    print("Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_task()
    elif choice == 2:
        view_tasks()
    elif choice == 3:
        break
    else:
        print("Invalid choice. Try again.")
