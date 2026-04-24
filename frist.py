import json
import os

FILE_NAME = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Add task
def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print("Task added!")

# View tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks):
        status = "✔" if task["done"] else "✘"
        print(f"{i + 1}. [{status}] {task['task']}")

# Mark task complete
def complete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to complete: ")) - 1
        tasks[index]["done"] = True
        save_tasks(tasks)
        print("Task completed!")
    except:
        print("Invalid input.")

# Delete task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        tasks.pop(index)
        save_tasks(tasks)
        print("Task deleted!")
    except:
        print("Invalid input.")

# Main menu
def main():
    tasks = load_tasks()

    while True:
        print("\n==== TO-DO LIST ====")
        print("1. View tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()