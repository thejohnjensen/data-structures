"""Radix sort module."""


def radix_sort(numbers):
    """Radix sort."""
    if not isinstance(numbers, (list, tuple)):
        raise TypeError('Please input a list or tuple.')
    sorting_list = []
    final_list = []
    buckets = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: []
    }
    for number in numbers:
        sorting_list.append(str(number)[::-1])
    sorting = True
    i = 0
    while sorting:
        sorting = False
        for str_num in sorting_list:
            try:
                buckets[int(str_num[i])].append(str_num)
                sorting = True
            except IndexError:
                buckets[0].append(str_num)
        sorting_list = []
        for bucket_key in range(10):
            for number_in_bucket in buckets[bucket_key]:
                sorting_list.append(number_in_bucket)
        buckets = {
            0: [],
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: []
        }
        i += 1

    for str_rev_num in sorting_list:
        final_list.append(int(str_rev_num[::-1]))
    return final_list


if __name__ == '__main__':
    radix_sort([100, 10, 99, 5, 999999, 52])
