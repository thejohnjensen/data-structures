"""."""


def return_index(array, key):
    low, high = 0, len(array) - 1
    mid = (high - low) // 2
    while low <= high:
        if array[mid] == key:
            if mid == 0:
                return 0
            elif array[mid - 1] == key:
                while array[mid] == key:
                    if mid == 0:
                        return 0
                    mid = mid - 1
                return mid + 1
            return mid
        if array[mid] > key:
            high = mid
            mid = (high - low) // 2
        else:
            low = mid
            mid = low + ((high - low) // 2) + 1
    return -1

