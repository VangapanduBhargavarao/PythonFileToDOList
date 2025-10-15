import os
TASKS="tasks.txt"
def load_tasks():
    if not os.path.exists(TASKS):
        return []
    else:
        with open(TASKS,"r") as fp:
            return fp.readlines() 
def show_tasks(tasks):
    print("your To-do list is:")
    if not tasks:
        print("no tasks in your list")
        return 
    for i ,task in enumerate(tasks,start=1):
        print(f"your task is {i}--->{task}")
    print('---------------------------------')
def save_tasks(tasks):
    with open(TASKS,"w") as fp:
        fp.writelines(tasks)
def add_task():
    task=input("enter your task add to your list:")
    tasks.append(f"[]{task}\n")
    save_tasks(tasks)
def mark_task():
    show_tasks(tasks)
    try:
        num=int(input("enter number to mark task"))
        if 1<=num<=len(tasks):
            if "[X]" in tasks[num-1]:
                print("your task is already Done")
            else:
                tasks[num-1]=tasks[num-1].replace("[]","[X]")
                save_tasks(tasks)
        else:
            print("enter valid number")
    except:
        print("giv the correct value")
def delete_task():
    show_tasks(tasks)
    try:
        num=int(input("enter number which task to be deleted"))
        if 1<=num<=len(tasks):
            deleted=tasks.pop(num-1)
            save_tasks(tasks)
            print(f"the task is deleted is:{deleted}")
        else:
            print("give the valid number")
    except ValueError:
        print("give the correct value for deleted")

tasks=load_tasks()
print(tasks)
while True:
    print("select one option for your choice")
    print("1.ShowTasks\n2.AddTask\n3.MarkTask\n4.DeleteTask\n5.Exit")
    try:
        choice=int(input("entetr the number"))
    except:
        print("you did not enter the input number") 
    else:
        match choice:
            case 1:show_tasks(tasks)
            case 2:add_task()
            case 3:mark_task()
            case 4:delete_task()
            case 5:break
            case _:print("INVALID OPTION TRY AGAIN")
