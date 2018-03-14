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


def rep_rem(a, val):
    out = []
    rules = {'a': ['d', 'd'], 'b': []}
    for i in range(val):
        # import pdb; pdb.set_trace()
        if a[i] in rules:
            for letter in rules[a[i]]:
                out.append(letter)
        else:
            out.append(a[i])

    return out


def rom_int(s):

    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    out = 0
    update = None
    for letter in s:
        val = values[letter]
        if update is None:
            update = val
        elif val > update:
            out += val - update
            update = None
        else:
            out += update
            update = val
    if update is not None:
        out += update
    return out


def phone_mnemonics(n):
    d = {'2': ['a','b','c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i']}
    output = d[n[0]]
    temp = []
    count = 1
    while count < len(n):
        # import pdb; pdb.set_trace()
        for i in output:
            for j in d[n[count]]:
                m = ''
                m = i + j
                temp.append(m)
        count += 1
        output = temp
        temp = []
    return len(output)


class Test(unittest.TestCase):
    def test_palindrom(self):
        self.assertEqual(is_palindrome('racecar'), True)


if __name__ == '__main__':
    unittest.main()
