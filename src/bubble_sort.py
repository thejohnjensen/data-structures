"""Bubble sort algorithm."""
import timeit


def bubble_sort(l):
    """Bubble Sort: Input list or tuple."""
    if not isinstance(l, (list, tuple)):
        raise TypeError('Please input a list or tuple.')
    n = len(l)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n - 1):
            j = i + 1
            if l[i] > l[j]:
                temp = l[j]
                l[j] = l[i]
                l[i] = temp
                swapped = True
    return(l)


if __name__ == '__main__':
    user_input = input('Input comma seperated numbers: ')
    input_list = user_input.split(',')
    numbers = [int(i) for i in input_list]
    print(bubble_sort(numbers))
    print('Time: {}'.format(timeit.timeit("bubble_sort(numbers)", setup="from __main__ import bubble_sort, numbers")))
