import sys
import time
start_time = time.time()

def summ_all(mixed_list: list):
    strings = ""
    numbers = 0
    lists = []
    tuples = ()
    for i in mixed_list:
        if type(i) == str:
            strings += i
        elif type(i) == int:
            numbers += i
        elif type(i) == list:
            lists += i
        elif type(i) == tuple:
            tuples += i
    return f"Sum -> strings:{strings},| numbers:{numbers},| lists:{sum(lists)},| tuples:{sum(tuples)}"


mixed_list = [1, 2.5, 'text', [4, 5, 6], (7, 8, 9),
              12, [5, 22, 86], "mama", (9, 23, 11)]
print(summ_all(mixed_list))

my_memory = sys.getsizeof(summ_all)
print("time elapsed: {:.2f}s".format(time.time() - start_time), "|", my_memory)

#____________________________________________________________________________________
import sys
import time

start_time = time.time()


def summ_all(mixed_list: list):
    result = mixed_list[0]
    for i in mixed_list[1:]:
        try:
            result += i
        except:
            pass

    return result


mixed_list = [1, 2.5, 'text', [4, 5, 6], (7, 8, 9),
              12, [5, 22, 86], "mama", (9, 23, 11)]
print(summ_all(mixed_list))

my_memory = sys.getsizeof(summ_all)
print("time elapsed: {:.2f}s".format(time.time() - start_time), "|", my_memory)
start_time = time.time()
#____________________________________________________________________________________

import sys
import time

start_time = time.time()


def summ_all(mixed_list: list):
    result = mixed_list[0]
    for i in mixed_list[1:]:
        if type(mixed_list[0]) == type(i):
            result += i

    return result


mixed_list = [1, 2.5, 'text', [4, 5, 6], (7, 8, 9),
              12, [5, 22, 86], "mama", (9, 23, 11)]
print(summ_all(mixed_list))

my_memory = sys.getsizeof(summ_all)
print("time elapsed: {:.2f}s".format(time.time() - start_time), "|", my_memory)
start_time = time.time()