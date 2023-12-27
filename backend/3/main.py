def task_1():
    print("Task 1: Create new list, which contains only users from Poland")

    users = [
        {"name": "Kamil", "country": "Poland"},
        {"name": "John", "country": "USA"},
        {"name": "Yeti"},
    ]

    polish_users = [user for user in users if user.get("country") == "Poland"]
    print(f"Answer: {polish_users}\n")


def task_2():
    print("Task 2: Display sum of first ten elements starting from element 5")

    numbers = [
        1,
        5,
        2,
        3,
        1,
        4,
        1,
        23,
        12,
        2,
        3,
        1,
        2,
        31,
        23,
        1,
        2,
        3,
        1,
        23,
        1,
        2,
        3,
        123,
    ]

    sum_of_ten = sum(numbers[5:15])
    print(f"Answer: {sum_of_ten}\n")


def task_3():
    print("Task 3: Fill list with powers of 2, n [1..20]")

    powers_of_two = [2**n for n in range(1, 21)]
    print(f"Answer: {powers_of_two}\n")


if __name__ == "__main__":
    task_1()
    task_2()
    task_3()
