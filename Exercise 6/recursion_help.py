
def find_all_permutes(lst, start, end):
    if start == end:
        print(lst)
    for i in range(start, end + 1):
        lst[start], lst[i] = lst[i], lst[start]
        find_all_permutes(lst, start + 1, end)
        lst[start], lst[i] = lst[i], lst[start]


def factorial(n):
    """ returns the factorial of n """
    if n <= 1:  # base case
        return 1
    elif n > 1:
        return n * factorial(n - 1)  # recursive call


def is_palindrome(n):
    """ returns True if n is palindrome, False otherwise """
    if len(n) == 1:
        return True
    elif n[0] != n[-1]:
        return False
    return is_palindrome(n[1:-1])


def addition_num(num_str):
    if len(num_str) == 2:
        return True
    elif int(num_str[0]) + int(num_str[1]) != int(num_str[2]):
        return False
    return addition_num(num_str[1:])


def sum_lst(lst):
    if len(lst) == 1:
        return lst[0]
    return lst[0] + sum_lst(lst[1:])


def a(start, end, step):
    print(start, end=' ')
    if start < end:
        a(start+step, end, step)
        print(start, end=' ')


def half_pyramid(n):
    if n < 1:
        return
    half_pyramid(n-1)
    print('*' * n)


def reversed_half(n):
    if n < 1:
        return
    print('*' * n)
    reversed_half(n - 1)


def full_pyramid(n):
    half_pyramid(n)
    reversed_half(n-1)
