# tasks=[]
# def main():
#      print("Welcome to the TO DO LIST APP:")
#      while True:
#         print("\n")
#         print("please select one of the following options")
#         print("---------------")
#         print("1.add a new task")
#         print("2.Delete a task")
#         print("3.List tasks")
#         print("4. Quit")
#         choice=input("enter your choice: ")
#         if (choice=='1'):
#             addTask()
#         elif (choice=='2'):
#             deleteTask()
#         elif (choice=='3'):
#             listTasks()
#         elif (choice=='4'):
#             break
#         else:
#             print("invalid input")


# def addTask():
#     task=input("please enter a task: ")
#     tasks.append(task)
#     print(f"Task '{task}' added to the list")

# def listTasks():
#     if not tasks:
#         print("there are no tasks currently")
#     else:
#         print("current task:")
#         for index,task in enumerate(tasks):
#             print(f"task *{index}.{task}")

# def deleteTask():
#     listTasks()
#     try:
#         taskToDelete=int(input("enter the # to delete:"))
#         if taskToDelete >=0 and taskToDelete< len(tasks):
#             tasks.pop(taskToDelete)
#             print(f"Task {taskToDelete} has been removed")

#         else:
#             print(f"task #{taskToDelete} was not found.")

#     except:
#         print("invalid input")


# if __name__=="__main__":
#     main()
tasks = []

def main():
    print("Welcome to the TO DO LIST APP:")
    while True:
        print("\n")
        print("Please select one of the following options")
        print("---------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            addTask()
        elif choice == '2':
            deleteTask()
        elif choice == '3':
            listTasks()
        elif choice == '4':
            break
        else:
            print("Invalid input")

def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list")

def listTasks():
    if not tasks:
        print("There are no tasks currently")
    else:
        print("Current tasks:")
        for index, task in enumerate(tasks):
            print(f"task #1{index+1}.{task}")

def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the number of the task to delete: ")) - 1
        if 0 <= taskToDelete < len(tasks):
            removed_task = tasks.pop(taskToDelete)
            print(f"Task '{removed_task}' has been removed")
        else:
            print(f"Task number {taskToDelete + 1} was not found.")
    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()

