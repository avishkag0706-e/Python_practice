# create a To-Do List program where the user can:

# Add a task
# View all tasks
# Remove a task
# Exit the program

tasks = []

while True:
    print("\n To do list")
    print("1. Add Task")
    print("2. view Tasks")
    print("3. Remove Task")
    print("4. Exit")
    
    choice = input("Enter your choice:")
    
    if choice =="1":
        task = input("Enter your task:")
        tasks.append(task)
        print("task addded successfully")
        print(tasks)
    elif choice =="2":
        if len(tasks) == 0:
            print("task is not there")
        else:
            print("\nYour Tasks:")
            
            for i in range(len(tasks)):
                print(i + 1,".",tasks[i])
    elif choice =="3":
        if len(tasks)==0:
            print("no tasks to remove")
        else:
            print("\nYour Tasks:")
            
            for i in range(len(tasks)):
                print(i + 1,".",tasks[i])
                
                task_number = int(input("Enter task number to remove:"))
                
                if task_number >=1 and task_number <=len(tasks):
                    remove_task = tasks.pop(task_number - 1)
                    print("removed:",remove_task)
                else:
                    print("Invalid task number.")
    elif choice =="4":
        print("goodbye!")
        break
    else:
        print("Invalid choice.please try again.")
                
                