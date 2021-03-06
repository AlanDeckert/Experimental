from collections import defaultdict

class Tasks:
    def __init__(self, task_id, earnings, start_time, end_time):
        self.task_id = task_id
        self.earnings = earnings
        self.start_time = start_time
        self.end_time = end_time
        self.duration = (end_time - start_time)


# ---------------------------------------------------------------- #
def add_tasks():
    task_continue = 'y'
    i = 1

    while task_continue == 'y' or task_continue == 'Y':
        try:
            task_earnings = int(input("Please enter the earnings value for this task:\n"))
            task_start = int(input("Please enter the start time for this task:\n"))
            task_end = int(input("Please enter the end time for this task:\n"))

            while task_end < task_start:
                task_end = int(input(f"Please select a task end time greater than the start time ({task_start}):\n"))

            task_list.append(Tasks(i, task_earnings, task_start, task_end))
            i += 1
            task_continue = input("Would you like to add another task? Y/N?\n")

        except ValueError:
            print("Please only use integer values")

    return task_list


# ---------------------------------------------------------------- #
def prev(n):
    n_start = task_list[n-1].start_time
    n_prev = 0

    # cycles through list of tasks
    for i, task in enumerate(task_list):
        # if n_prev has been changed from its initial value of 0
        if n_prev > 0:
            # finds the latest task end time that's less than or equal to the start of n
            if n_start >= task.end_time > task_list[n_prev-1].end_time:
                n_prev = task.task_id
        else:
            # else, n_prev is 0 and assigns it to the first task that ends before n starts
            if n_start >= task.end_time:
                n_prev = task.task_id

    return n_prev


# ---------------------------------------------------------------- #
def get_max(n):

    if n == 0:
        return 0

    previous = prev(n)

    if previous in path_dict:
        do_task = value(n) + value_dict[previous][0]

    else:
        do_task = value(n) + get_max(previous)

    if n-1 in path_dict:
       dont_do_task = value_dict[n-1][0]
    else:
        dont_do_task = get_max(n-1)

    if do_task > dont_do_task:
        if n not in path_dict:
            if previous > 0:
                for path in path_dict[previous]:
                    path_dict[n].append(path)

            path_dict[n].append(n)

            value_dict[n].append(do_task)

        return do_task

    # otherwise, return the value for not doing the task
    else:
        if n not in path_dict:

            for path in path_dict[n-1]:
                path_dict[n].append(path)

            value_dict[n].append(dont_do_task)

        return dont_do_task


# ---------------------------------------------------------------- #
def value(n):
    n_value = task_list[n-1].earnings
    return n_value


# ---------------------------------------------------------------- #
# takes a number n and the list of all tasks
def calculate():
    for i in range(8):
        get_max(i+1)


# ---------------------------------------------------------------- #
def user_menu():
    option_list = [1, 2, 3, 4]
    user_input = -2

    while user_input != 4:
        try:
            user_input = int(input("Please select from the following options:\n"
                                   "1. Enter new Tasks\n"
                                   "2. View All Tasks\n"
                                   "3. Delete a Task\n"
                                   "4. Exit Program (Data will be lost)\n"))

            if user_input not in option_list:
                print("Please choose a number from 1 - 4")

            if user_input == 1:
                task_list = add_tasks()

            # elif user_input == 2:
            # elif user_input == 3:
            # elif user_input == 4:

        except ValueError:
            print("Please enter an integer value")

    return task_list


if __name__ == '__main__':
    task_list = [
        Tasks(1, 5, 1, 4),
        Tasks(2, 1, 3, 5),
        Tasks(3, 8, 0, 6),
        Tasks(4, 4, 4, 7),
        Tasks(5, 6, 3, 8),
        Tasks(6, 3, 5, 9),
        Tasks(7, 2, 6, 10),
        Tasks(8, 4, 8, 11)
    ]

    value_dict = defaultdict(list)
    path_dict = defaultdict(list)

    calculate()
    print(path_dict)

