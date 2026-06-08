import functools


def double_letter(my_str):
    return ''.join(char * 2 for char in my_str)


def check_div(number):
    return number % 4 == 0


def four_dividers(number):
    return list(filter(check_div, range(number)))

def add(x,y):
    return x + y


def sum_of_digits(number):
    return functools.reduce(add, map(int, str(abs(number))))


def intersection(list_1, list_2):
    return [x for x in set(list_1) if x in set(list_2)]


def is_funny(string):
    return len(string) and list(string) == [char for char in string if char == 'h' or char == 'a']

def main():
    print(double_letter("python"))
    print(double_letter("we are the champions!"))
    print(four_dividers(9))
    print(four_dividers(3))
    print(sum_of_digits(104))
    print(intersection([1, 2, 3, 4], [8, 3, 9]))
    print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))
    print(is_funny("hahahahahaa"))



if __name__ == "__main__":
    main()