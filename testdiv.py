import unittest
from calcbao.calcdemo import calc
from ddt import ddt
from ddt import data
from ddt import unpack

data1=[
    [6,3,2],
    [20,4,5]
]
@ddt
class  testDIVI(unittest.TestCase):
    @data(*data1)
    @unpack

    def testdiv(self,x,y,z):
        a=x
        b=y
        s=z

        c=calc()

        sum=c.div(a,b)

        self.assertEqual(s,sum)