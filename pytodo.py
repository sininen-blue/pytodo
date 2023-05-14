# add
# complete
# delete
# reprioritize
# deprioritize
# list
todo_file = "todo.txt"

def get_all_tasks():
    all_tasks = []
    
    with open(todo_file, "r") as file:
        all_tasks = file.readlines()

    return all_tasks

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

add_task("testing2")


