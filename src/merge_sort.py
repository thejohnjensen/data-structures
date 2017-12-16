"""Module for merge sort."""
import timeit


def merge_sort(l):
    """Merge sort takes an a list and divides them into smaller lists and then.

    sort the sublists.
    """
    if not isinstance(l, (list, tuple)):
        raise TypeError('Please input a list or tuple.')
    mid = int(len(l) / 2)
    if len(l) > 1:
        a = merge_sort(l[:mid])
        b = merge_sort(l[mid:])
        return merge(a, b)
    else:
        return l


def merge(a, b):
    """
    Helper function that sorts each of the smaller arrays from merge_sort.

    Help from:
    https://codereview.stackexchange.com/questions/154135/recursive-merge-sort-in-python.
    """
    merged = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    merged += a[i:]
    merged += b[j:]
    return merged


if __name__ == '__main__':
    user_input = input('Input comma seperated numbers: ')
    input_list = user_input.split(',')
    numbers = [int(i) for i in input_list]
    print(merge_sort(numbers))
    print('Time: {}'.format(timeit.timeit("merge_sort(numbers)", setup="from __main__ import merge_sort, numbers")))