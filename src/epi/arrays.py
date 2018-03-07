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


class Test(unittest.TestCase):
    def test_dutch_flag_part(self):
        self.assertEqual(dutch_flag_part([0, 1, 2, 0, 1], 3), [0, 0, 1, 2, 1])

    def test_stocks(self):
        self.assertEqual(max_stock_sale([10, 20, 5, 35, 15]), 30.0)


if __name__ == '__main__':
    unittest.main()