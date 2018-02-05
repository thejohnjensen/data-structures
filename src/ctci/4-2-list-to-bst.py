from src.bst import Node


# def list_to_bst(arr, start, end):
#     """."""
#     import pdb; pdb.set_trace()
#     if(start > end):
#         return None
#     mid = (start + end) // 2
#     n = Node(arr[mid])
#     n.left = list_to_bst(arr, start, mid - 1)
#     n.right = list_to_bst(arr, mid + 1, end)

#     return n


def list_to_bst(arr):
    # import pdb; pdb.set_trace()
    if(len(arr) < 1):
        return None
    mid = len(arr) // 2
    n = Node(arr[mid])
    n.left = list_to_bst(arr[:mid])
    n.right = list_to_bst(arr[mid + 1:])

    return n

if __name__ == '__main__':
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # bst = list_to_bst(arr, 0, len(arr) - 1)
    bst = list_to_bst(arr)
