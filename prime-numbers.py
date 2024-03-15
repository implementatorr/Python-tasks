def foo(start, stop):
    result = []
    for i in range(start, stop + 1):
        flag = True
        num_str = str(i)
        num = sum(int(j) for j in num_str)
        if num % 2 == 0 or num % 3 == 0:
            continue

        for k in range(2, i // 2 + 1):
            if i % k == 0:
                flag = False
                break
        if flag:
            result.append(i)

    return result


start = int(input("Start :"))
end = int(input("End :"))
print((foo(start, end)))

###################################################################################

import sys
import time

start_time = time.time()


def foo(start, stop):
    result = []
    for i in range(start, stop + 1):
        flag = True
        if i % 2 == 0 or i % 3 == 0:
            continue

        for k in range(2, i // 2):
            if i % k == 0:
                flag = False
                break
        if flag:
            result.append(i)

    return result


start = int(input("Start :"))
end = int(input("End :"))
print((foo(start, end)))

my_memory = sys.getsizeof(foo(start, end))
print("time elapsed: {:.2f}s".format(time.time() - start_time))
print(my_memory)