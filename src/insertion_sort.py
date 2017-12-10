"""."""
import timeit


def insertion(l):
    """."""
    if not isinstance(l, (list, tuple)):
        raise TypeError('Please input a list or tuple.')
    i = 1
    while i < len(l):
        j = i
        while j > 0 and l[j - 1] > l[j]:
            temp = l[j]
            l[j] = l[j - 1]
            l[j - 1] = temp
            j -= 1
        i += 1
    return l

if __name__ == '__main__':
    user_input = input('Input comma seperated numbers: ')
    input_list = user_input.split(',')
    numbers = [int(i) for i in input_list]
    print(insertion(numbers))
    print('Time: {}'.format(timeit.timeit("insertion(numbers)", setup="from __main__ import insertion, numbers")))
