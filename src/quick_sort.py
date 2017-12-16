"""Quicsort Module."""
import timeit


def quicksort(arr):
    """Call helper function."""
    if not isinstance(arr, (list, tuple)):
        raise TypeError('Please input a list or tuple.')
    return _helper(arr, 0, len(arr) - 1)


def _helper(arr, left, right):
    """Recusively divide and sort."""
    if left < right:
        div = partition(arr, left, right)
        _helper(arr, left, div[2] - 1)
        _helper(arr, div[2] + 1, right)
    return arr


def partition(arr, left, right):
    """Funciton to partition list."""
    pivot = left
    i, j = left + 1, right
    while True:
        while i <= j and arr[i] < arr[pivot]:
            i += 1
        while j >= i and arr[j] > arr[pivot]:
            j -= 1
        if j < i:
            break
        else:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
    temp = arr[pivot]
    arr[pivot] = arr[j]
    arr[j] = temp
    return arr, i, j


if __name__ == '__main__':
    user_input = input('Input comma seperated numbers: ')
    input_list = user_input.split(',')
    numbers = [int(i) for i in input_list]
    print(quicksort(numbers))
    print('Time: {}'.format(timeit.timeit("quicksort(numbers)", setup="from __main__ import quicksort, numbers")))
