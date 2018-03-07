"""."""
import unittest


def is_palindrome(s):
    """."""
    start = 0
    end = len(s) - 1
    palindrom = True
    while palindrom:
        if s[start] != s[end]:
            palindrom = False
        elif start == end or start > end:
            return True
        else:
            start += 1
            end -= 1
    return palindrom


class Test(unittest.TestCase):
    def test_palindrom(self):
        self.assertEqual(is_palindrome('racecar'), True)


if __name__ == '__main__':
    unittest.main()