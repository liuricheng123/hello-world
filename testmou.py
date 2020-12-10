import unittest
from calcbao.calcdemo import calc
from ddt import ddt
from ddt import data
from ddt import unpack

data1=[
    [2,3,6],
    [4,5,20]
]
@ddt
class  testMOU(unittest.TestCase):
    @data(*data1)
    @unpack

    def testmou(self,x,y,z):
        a=x
        b=y
        s=z

        c=calc()

        sum=c.mou(a,b)

        self.assertEqual(s,sum)