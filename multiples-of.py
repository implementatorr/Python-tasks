def input_dig():
    while True:
        digit = input("Pleas enter a digit: ")
        if digit.isalpha():
            continue
        elif int(digit) <= 0:
            continue
        else:
            return int(digit)


def check_digit(digit: int):
    counter = 0
    list_of = []
    for counter in range(1, digit):
        if digit % counter == 0:
            list_of.append(counter)
    return list_of


digit = input_dig()
print(check_digit(digit))