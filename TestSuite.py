import unittest

from test_files.TestExponential import TestExponential
from test_files.TestGamma import TestGamma
from test_files.TestPoisson import TestPoisson
from test_files.TestMle import TestMle
from test_files.TestPlot import TestPlot
from test_files.TestSummary import TestSummary 

def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestExponential))
    suite.addTest(unittest.makeSuite(TestGamma))
    suite.addTest(unittest.makeSuite(TestPoisson))
    suite.addTest(unittest.makeSuite(TestMle))
    suite.addTest(unittest.makeSuite(TestPlot))
    suite.addTest(unittest.makeSuite(TestSummary))

    runner = unittest.TextTestRunner()
    print(runner.run(suite))

my_suite()