import unittest
"""Module for primitive types section."""

# 4.1 Computing parity of a word
# 0 if 1s in word are even
# 1 if 1s in word are odd

# def parity(x):
#     """."""
#     result = 0
#     while x:
#         result ^= x & 1
#         x >>= 1
#     return result


def parity(x):
    """."""
    result = 0
    while x:
        result ^= 1
        x &= x - 1
    return result


class Test(unittest.TestCase):
    def test_parity(self):
        self.assertEqual(parity(9), 0)

if __name__ == '__main__':
    unittest.main()

