import sys
import time

start_time = time.time()


def foo(strs):
    if len(strs) <= 1:
        return "".join(strs)
    else:
        result = ""
        for k, i in enumerate(strs[0]):
            flag = False
            n = 1
            while n <= len(strs) - 1:
                if len(strs[n]) == 0:
                    return ""
                if k <= len(strs[n]) - 1:
                    if i == strs[n][k]:
                        flag = True
                    else:
                        flag = False
                        return result
                else:
                    return result
                n += 1
            if True is flag:
                result += i

        return result


strs = ["aaa", "aa", "aaa"]
print(foo(strs))

my_memory = sys.getsizeof(foo)
print("time elapsed: {:.2f}s".format(time.time() - start_time), "|", my_memory)