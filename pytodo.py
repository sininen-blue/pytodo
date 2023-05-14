# add
# complete
# delete
# reprioritize
# deprioritize
# list

def add_task(task, index = -1):
    if index == -1:
        file = open("todo.txt", "a")
        file.write(f"{task}\n")
        file.close()
    else:
        all_tasks = []

        file = open("todo.txt", "r")
        for item in file:
            all_tasks.append(item)
        file.close()
       
        all_tasks.insert(index-1, f"{task}\n")
        file = open("todo.txt", "w")
        file.writelines(all_tasks)

