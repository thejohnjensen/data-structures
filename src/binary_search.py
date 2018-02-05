"""Algo to implement binary search."""


def binary_search(elements, target):
    """."""
    mid = len(elements) // 2
    if len(elements) == 0:
        return False
    if elements[mid] == target:
        return True
    if target < elements[mid]:
        return binary_search(elements[:mid], target)
    else:
        return binary_search(elements[mid + 1:], target)
    

if __name__ == '__main__':
    print(binary_search([9,10,11], 12))