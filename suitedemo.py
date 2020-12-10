import unittest
import os

from HTMLTestRunner import HTMLTestRunner

suite=unittest.TestSuite()

loader=unittest.defaultTestLoader

cases=loader.discover(os.getcwd(),pattern="test*.py")
suite.addTest(cases)
f=open("加法.html","w+",encoding="utf-8")
html=HTMLTestRunner.HTMLTestRunner(
    stream=f,
    title="加法",
    description="加法",
    verbosity=1
)

html.run(suite)