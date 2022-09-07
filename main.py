import random
from typing import Callable


def bogo_sort(l, iteration=1):
    print(f"{iteration=}")
    for x in range(len(l)):
        if x < len(l) - 1:
            if not (l[x] <= l[x + 1]):
                random.shuffle(l)
                return bogo_sort(l, iteration + 1)


def stalin_sort(l):
    current = l[0]
    sorted_l = []
    for x in l:
        if x >= current:
            sorted_l.append(x)
            current = x
    return sorted_l


def test_sort(sorting_func: Callable, element_count=10, min_val=1, max_val=20):
    test_list = [random.randint(min_val, max_val) for x in range(element_count)]

    print(test_list)

    list_copy = list(test_list)  # shallow copy

    try:
        sorted_list = sorting_func(list_copy)
        if not sorted_list is None:
            list_copy = sorted_list
        test_list.sort()

        print(list_copy, test_list)
    except Exception as e:
        print(e)


def main():
    test_sort(bogo_sort, element_count=5)


if __name__ == "__main__":
    main()
