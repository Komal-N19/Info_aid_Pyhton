import json

class Task:
    def __init__(self, title, description, status="Incomplete"):
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\nStatus: {self.status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Task '{removed_task.title}' removed!")
        else:
            print("Invalid task index.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks to display.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task.title}")

    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            task_list = [vars(task) for task in self.tasks]
            json.dump(task_list, file)
        print("Tasks saved to file.")

    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as file:
                task_list = json.load(file)
                self.tasks = [Task(**task) for task in task_list]
            print("Tasks loaded from file.")
        except FileNotFoundError:
            print("File not found. No tasks loaded.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Delete a task")
        print("4. Save tasks to file")
        print("5. Load tasks from file")
        print("6. Quit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == "1":
            title = input("Enter the task title: ")
            description = input("Enter the task description: ")
            task = Task(title, description)
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            todo_list.view_tasks()
            task_index = int(input("Enter the index of the task to delete: "))
            todo_list.delete_task(task_index)
        elif choice == "4":
            filename = input("Enter the filename to save tasks: ")
            todo_list.save_tasks(filename)
        elif choice == "5":
            filename = input("Enter the filename to load tasks from: ")
            todo_list.load_tasks(filename)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option (1/2/3/4/5/6).")

if __name__ == "__main__":
    main()
