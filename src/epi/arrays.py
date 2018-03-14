"""Module for chp 5 arrays."""

import unittest


def dutch_flag_part(a, p):
    """."""
    pivot = a[p]
    s = []
    e = []
    b = []
    for val in a:
        if val > pivot:
            b.append(val)
        elif val == pivot:
            e.append(val)
        else:
            s.append(val)
    return s + e + b


def max_stock_sale(prices):
    """."""
    min_price = float('Inf')
    max_sales = 0.0
    for price in prices:
        if price < min_price:
            min_price = price
        if price - min_price > max_sales:
            max_sales = price - min_price
    return max_sales


import random


def sample(a, s):
    l = len(a) - 1
    indxs = set()
    for _ in range(s):
        rand = random.randrange(l)
        while rand in indxs:
            rand = random.randrange(l)
        indxs.add(rand)
    output = []
    for i in indxs:
        output.append(a[i])
    a[:] = output
    # for i in range(s):
    #     import pdb; pdb.set_trace()
    #     rand = random.randint(i, l)
    #     a[i], a[rand] = a[rand], a[i]
    # A[:] = random.sample(A, k)


def quicksort(l):
    """
    TODO: implement recursion.
    """
    piv = len(l) - 1
    wall = 0

    for j in range(len(l)):
        if l[j] < l[piv]:
            # swap l[j] with wall value
            l[j], l[wall] = l[wall], l[j]
            # increment wall
            wall += 1
    # swap piv with wall
    l[wall], l[piv] = l[piv], l[wall]
    return l


class Test(unittest.TestCase):
    def test_dutch_flag_part(self):
        self.assertEqual(dutch_flag_part([0, 1, 2, 0, 1], 3), [0, 0, 1, 2, 1])

    def test_stocks(self):
        self.assertEqual(max_stock_sale([10, 20, 5, 35, 15]), 30.0)


if __name__ == '__main__':
    unittest.main()
