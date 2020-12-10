import unittest
from calcbao.calcdemo import calc
from ddt import ddt
from ddt import data
from ddt import unpack

data1=[
    [1,2,3],
    [4,5,9]
]
@ddt
class  testsige(unittest.TestCase):
    @data(*data1)
    @unpack

    def testadd(self,x,y,z):
        a=x
        b=y
        s=z

        c=calc()

        sum=c.add(a,b)

        self.assertEqual(s,sum)










