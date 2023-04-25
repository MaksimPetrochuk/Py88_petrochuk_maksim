from datetime import datetime


def decorator(func):
    def the_racer():
        time_1 = datetime.now()
        func()
        time_2 = datetime.now()
        time = time_2 - time_1
        print(time)
    return the_racer


@decorator
def func_1():
    word = 'kak?'
    res = str(word) * 40
    print(res)


@decorator
def func_2():
    num = 12
    res_1 = num % 2
    res_2 = num ** 148
    print(res_1)
    print(res_2)


func_1()
func_2()

