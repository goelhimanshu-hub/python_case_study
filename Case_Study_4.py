import os

FILE_NAME = "tasks.txt"

# Ensure file exists
if not os.path.exists(FILE_NAME):
    open(FILE_NAME, "w").close()


# -------- Add Task --------
def add_task():
    task_id = input("Enter Task ID: ")
    desc = input("Enter Task Description: ")
    status = "Pending"

    with open(FILE_NAME, "a") as f:
        f.write(f"{task_id}|{desc}|{status}\n")

    print("✅ Task Added Successfully!")


# -------- View Tasks --------
def view_tasks():
    with open(FILE_NAME, "r") as f:
        tasks = f.readlines()

    if not tasks:
        print("⚠️ No tasks found.")
        return

    print("\n--- Task List ---")
    for task in tasks:
        task_id, desc, status = task.strip().split("|")
        print(f"ID: {task_id} | Task: {desc} | Status: {status}")
    print("------------------\n")


# -------- Update Task --------
def update_task():
    task_id = input("Enter Task ID to update: ")

    with open(FILE_NAME, "r") as f:
        tasks = f.readlines()

    found = False
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            t_id, desc, status = task.strip().split("|")

            if t_id == task_id:
                found = True
                print("1. Update Description")
                print("2. Mark as Completed")
                choice = input("Choose option: ")

                if choice == "1":
                    desc = input("Enter new description: ")
                elif choice == "2":
                    status = "Completed"

                f.write(f"{t_id}|{desc}|{status}\n")
            else:
                f.write(task)

    if found:
        print("✅ Task Updated!")
    else:
        print("❌ Task ID not found.")


# -------- Delete Task --------
def delete_task():
    task_id = input("Enter Task ID to delete: ")

    with open(FILE_NAME, "r") as f:
        tasks = f.readlines()

    found = False
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            t_id, desc, status = task.strip().split("|")

            if t_id != task_id:
                f.write(task)
            else:
                found = True

    if found:
        print("🗑️ Task Deleted!")
    else:
        print("❌ Task ID not found.")


# -------- Search Task --------
def search_task():
    keyword = input("Enter Task ID or keyword: ")

    with open(FILE_NAME, "r") as f:
        tasks = f.readlines()

    found = False
    for task in tasks:
        if keyword in task:
            t_id, desc, status = task.strip().split("|")
            print(f"ID: {t_id} | Task: {desc} | Status: {status}")
            found = True

    if not found:
        print("❌ No matching task found.")


# -------- Menu --------
def menu():
    while True:
        print("\n====== TO-DO NOTES BUILDER ======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Search Task")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            search_task()
        elif choice == "6":
            print("👋 Exiting...")
            break
        else:
            print("⚠️ Invalid choice!")


# Run Program
menu()
