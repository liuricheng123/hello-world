import unittest
from ddt import data
from ddt import unpack
from ddt import ddt
from entityrw.bank16 import bank_addUser
from Utilsrw.DataRead import DataRead

data1=DataRead("database",database="day16",tablename="bankuser",user="root",password="",host="localhost").list
@ddt
class TestBankAddUser(unittest.TestCase):

    @data(*data1)
    @unpack
    def testAddUser(self,username,password,country,province,street,door,money,s):
        b=bank_addUser(username,password,country,province,street,door,money)

        self.assertEqual(s,b)

data2 = DataRead("database",database="day16",tablename="bankuser1",user="root",password="",host="localhost").list
@ddt
class TestBankAddUser1(unittest.TestCase):
    @data(*data2)
    @unpack
    def testAddUser1(self,username,password,country,province,street,door,money,s):
        # 实际结果
        bank_addUser(username,password,country,province,street,door,money)
        # 实际测试
        result = bank_addUser(username=username,password=password,country=country,province=province,street=street,door=door,money=money)
        self.assertEqual(result,s)

data3 = DataRead("database",database="day16",tablename="bankuser2",user="root",password="",host="localhost").list
@ddt
class TestBankAddUser2(unittest.TestCase):
    @data(*data3)
    @unpack
    def testAddUser2(self,username,password,country,province,street,door,money,s):
        for i in range(100):
            username = "张岩" + str(i)
            bank_addUser(username,password,country,province,street,door,money)
        result = bank_addUser(username=username,password=password,country=country,province=province,street=street,door=door,money=money)
        self.assertEqual(result,s)



