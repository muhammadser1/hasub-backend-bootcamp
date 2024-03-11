from tabulate import tabulate

class Task:
    def __init__(self, name, duration, specific_day, starting_hour):
        self.name = name
        self.duration = duration


def print_tasks():
    for day in days:
        print(' '.join(str(task.name) if task != 0 else '0' for task in day))

def delete(list,name):
    for i in range(len(list)):
        if list[i]!=0:
            if list[i].name==name:
                list[i]=0
##  name, duration, type_input
def get_input():
    name = input("Please write task name:")
    flag = 1
    while flag:
        duration = input("Please write task duration: (1-8) hours")
        if duration.isdigit() == 1:
            duration = (int)(duration)
            if duration >= 1 and duration <= 8:
                flag = 0
        if flag == 1:
            print("Please fill correct input.")
    flag = 1
    while flag:
        print("1. Choose specific day and hour?")
        print("2. Not choose specific day and hour")
        type_input = input("")
        if type_input.isdigit() == 1:
            type_input = (int)(type_input)
            if type_input >= 1 and type_input <= 2:
                flag = 0
        if flag == 1:
            print("Please fill correct input.")

    return name, duration, type_input
def print_already_task(days,day,start):
    j = start
    while j <= duration:
        if days[day][j] != 0:
            print("There is already a task scheduled at this time:   " + days[day][j].name)
        j += 1
def overwrite(days,day,start,duration):
    delete(days[day],days[day][start].name)
    j=start
    while j <= duration:
        days[day][j] = Task(name, duration, day, j)
        j+=1

##  specific day and start hour
def get_day_hour():
    flag = 1
    while flag:
        day = input("Select the day for the task (0-4)")
        if day.isdigit() == 1:
            day = (int)(day)
            if day >= 0 and day <= 4:
                start = input("Please write start  hour (0-8)")
                if start.isdigit() == 1:
                    start = (int)(start)
                    if start >= 0 and start <= 8:
                        flag = 0
        if flag == 1:
            print("Please fill correct input.")
    return day, start


## max_count, index
def max_None_continuity(lst):
    cur = 0
    index = 0
    count = 0
    max_count = 0
    for i in range(len(lst)):
        if lst[i] == 0:
            count += 1
            if count > max_count:
                max_count = count
                index = cur
        else:
            count = 0
            cur = i + 1

    return max_count, index


##Fill task if not on a specific day.
def find_empty_spot(days, name, duration):
    j = 0
    for i in range(len(days)):
        max_count, index = max_None_continuity(days[i])
        if max_count >= duration:
            task = Task(name, duration, i, index)
            while j < duration:
                days[i][index + j] = task
                j += 1
            print("Task Population Confirmation")
            return "ok"
            break
    else:
        print("No empty spot found for the task.")
    return "failed"


##Fill task if not on a specific day.
def fill_specific_time(day, duration, start, days, name):
    j = 0
    for i in range(start, len(days[day])):
        if days[day][i] == 0:
            j += 1
        if j >= duration:
            task = Task(name, duration, day, start)
            while start <= duration:
                days[day][start] = task
                start += 1
            print("Task Population Confirmation")
            return "ok"
            break
        if days[day][i] != 0:
            break
    return "failed"

def type_input_is_one(days,name,duration):
    day, start = get_day_hour()
    result = fill_specific_time(day, duration, start, days, name)
    while result == "failed":
        print_already_task(days,day,start)
        print("1.overwrite the old tasks?\n")
        print("2.give new time for new task?")
        flag = 1
        while flag:
            type_input = input("")
            if type_input.isdigit() == 1:
                type_input = (int)(type_input)
                if type_input >= 1 and type_input <= 2:
                    if type_input==2:
                        day, start = get_day_hour()
                        result = fill_specific_time(day, duration, start, days, name)
                    if type_input==1:
                        overwrite(days,day,start,duration)
                        print("Task Population Confirmation")
                        return "ok"
                    flag=0
            if flag==1:
                print("Please fill correct input.")
if __name__ == "__main__":
    days = [[0 for _ in range(9)] for _ in range(5)]
    for i in range(2):
        name, duration, type_input = get_input()
        if type_input == 2:  # no specific day,hour
            find_empty_spot(days, name, duration)
        if type_input == 1:
            type_input_is_one(days,name,duration)
    print_tasks()
    just_names=[]
    final=[]
    for i in range(len(days)):
        just_names=[]
        just_names.append("day"+str(i))
        for j in range(9):
            if days[i][j]!=0:
                just_names.append(days[i][j].name)

            else:
                just_names.append(0)
        final.append(just_names)
    hours=[]
    for i in range(9):
        hours.append("hour"+str(i))
    table = [hours]
    for i in range(len(days)):
        table.append(final[i])
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))