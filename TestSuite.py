import unittest

from TestExponential import TestExponential
from TestGamma import TestGamma
from TestPoisson import TestPoisson
from TestMle import TestMle
from TestPlot import TestPlot
from TestSummary import TestSummary 

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