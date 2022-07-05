# import sys
# sys.setrecursionlimit(n)
# Task1
def countdown(number):
    if number == 0:
        print(0)

    else:
        print(number)
        countdown(number-1)


# Task 2
def factorial(number):
    if number == 0:
        return 1
    if number == 1:
        return 1
    else:
        return number*factorial(number-1)


# Task 3
def harmonic_sum(number):
    if number < 1:
        return 0
    else:
        return 1/number + harmonic_sum(number-1)


if __name__ == '__main__':
    # countdown(5)

    # print(factorial(0))
    # print(factorial(1))
    # print(factorial(10))
    print(harmonic_sum(7))
    print(harmonic_sum(4))

