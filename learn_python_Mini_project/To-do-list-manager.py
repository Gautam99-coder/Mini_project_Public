def display_menu():
    print("\nTo-Do List Manager")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks(todo_list):
    if not todo_list:
        print("Your to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def add_task(todo_list):
    task = input("Enter the task: ")
    todo_list.append(task)
    print(f"Task '{task}' added successfully!")

def complete_task(todo_list):
    view_tasks(todo_list)
    if todo_list:
        try:
            task_num = int(input("Enter task number to mark as complete: ")) - 1
            if 0 <= task_num < len(todo_list):
                print(f"Task '{todo_list[task_num]}' marked as complete!")
                todo_list.pop(task_num)
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

def delete_task(todo_list):
    view_tasks(todo_list)
    if todo_list:
        try:
            task_num = int(input("Enter task number to delete: ")) - 1
            if 0 <= task_num < len(todo_list):
                print(f"Task '{todo_list[task_num]}' deleted!")
                todo_list.pop(task_num)
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

def todo_list_manager():
    todo_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            view_tasks(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            complete_task(todo_list)
        elif choice == '4':
            delete_task(todo_list)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-5.")

if __name__ == "__main__":
    todo_list_manager()
