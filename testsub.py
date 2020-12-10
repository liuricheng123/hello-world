import unittest
from calcbao.calcdemo import calc
from ddt import ddt
from ddt import data
from ddt import unpack

data2 = [
    [1, 2, -1],
    [4, 5, -1]
]


@ddt
class testsige(unittest.TestCase):
    @data(*data2)
    @unpack
    def testsub(self, x, y, z):
        a = x
        b = y
        s = z

        c = calc()

        sum = c.sub(a, b)

        self.assertEqual(s, sum)