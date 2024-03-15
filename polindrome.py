# this, using a lot of memory
def multi_l():
    my_range = range(100, 102)
    counter = 1
    start = 1
    list_of = []

    while start < len(my_range):
        for i in my_range:
            start += 1
            for k in my_range:
                counter = k * i
                list_of.append(counter) if counter not in list_of else counter
                list_of.sort()

    return list_of


def palindromic_check(x):
    pal_list = []
    for i in x:
        i = str(i)
        pol_number = i[::-1]
        if i == pol_number and int(i) > 10:
            pal_list.append(i)

    print(min(pal_list))


x = multi_l()
palindromic_check(x)

#________________________________


def multi_l():
    my_range = range(100, 1000)
    start = 1
    list_of = []
    while start < len(my_range):
        for i in my_range:
            start += 1
            for k in my_range:
                counter = k * i
                counter = str(counter)
                pol_number = counter[::-1]
                if counter == pol_number and int(counter) > 10:
                    list_of.append(int(counter))

    print(max(list_of))


multi_l()