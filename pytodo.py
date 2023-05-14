# add
# complete
# delete
# reprioritize
# deprioritize
# list
import sys

todo_file_location = "/home/sininenblue/.config/pytodo/"
todo_file = f"{todo_file_location}todo.txt"

def get_all_tasks():
    all_tasks = []
    
    with open(todo_file, "r") as file:
        all_tasks = file.readlines()

    return all_tasks

def list_tasks():
    all_tasks = get_all_tasks()
    
    task_index = 1
    for task in all_tasks:
        task = task.strip("\n")
        print(f"{task_index} {task}")

        task_index += 1


def add_task(task, index = -1):
    if index == -1:
        file = open(todo_file, "a")
        file.write(f"{task}\n")
        file.close()
    else:
        all_tasks = get_all_tasks()

        all_tasks.insert(index-1, f"{task}\n")
        
        file = open(todo_file, "w")
        file.writelines(all_tasks)
        file.close()

def done_task():
    all_tasks = get_all_tasks()
    all_tasks.pop(0)

    file = open(todo_file, "w")
    file.writelines(all_tasks)
    file.close()

def prioritize_task(task_index):
    if task_index == 1:
        print("can't prioritize task")
        return

    all_tasks = get_all_tasks()
    all_tasks.insert(0, all_tasks.pop(task_index - 1))

    with open(todo_file, "w") as file:
        file.writelines(all_tasks)

def deprioritize_task(task_index):
    all_tasks = get_all_tasks()
    all_tasks.append(all_tasks.pop(task_index - 1))

    with open(todo_file, "w") as file:
        file.writelines(all_tasks)


match sys.argv[1]:
    case "list":
        list_tasks()
    case "add":
        if len(sys.argv) == 4:
            add_task(sys.argv[2], int(sys.argv[3]))
        else:
            add_task(sys.argv[2])
    case "done":
        done_task()
    case "prio":
        prioritize_task(int(sys.argv[2]))
    case "deprio":
        deprioritize_task(int(sys.argv[2]))
    case _:
        print("not a valid command")

