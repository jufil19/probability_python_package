import unittest
import pandas as pd
import numpy
from distributions.estimation import plot 

class TestPlot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.expfile = 'exp_rate4.csv'
        cls.gammafile = 'gamme_shape2_rate4.csv'
        cls.poisfile = 'pois_rate4.csv'

        exp = pd.read_csv(cls.expfile)
        cls.exp = exp.iloc[:, 0].tolist()
        gamma = pd.read_csv(cls.gammafile)
        cls.gamma = gamma.iloc[:, 0].tolist()
        pois = pd.read_csv(cls.poisfile)
        cls.pois = pois.iloc[:, 0].tolist()
    @classmethod
    def tearDownClass(cls):
        pass
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_hist(self):
        self.assertIsInstance(plot.hist('gamma',self.gamma), numpy.ndarray)
        self.assertIsNotNone(plot.hist('gamma',self.gamma))
        self.assertGreater(len(plot.hist('gamma',self.gamma)), 0)
        self.assertGreaterEqual(min(plot.hist('exponential',self.exp)), 0)
        self.assertGreaterEqual(min(plot.hist('poisson',self.pois)), 0)

    def test_qqplot(self):
        self.assertIsInstance(plot.qqplot('gamma',self.gamma)[0][0], numpy.ndarray)
        self.assertIsInstance(plot.qqplot('gamma',self.gamma)[0][1], numpy.ndarray)
        self.assertGreaterEqual(min(plot.qqplot('exponential',self.exp)[0][0]), 0)
        self.assertGreaterEqual(min(plot.qqplot('poisson',self.pois)[0][0]), 0)
        self.assertGreaterEqual(min(plot.qqplot('gamma',self.gamma)[0][0]), 0)
        
    def test_boxplot(self):
        self.assertIsInstance(plot.boxplot(self.gamma), dict)
        self.assertIsInstance(plot.boxplot(self.exp), dict)
        self.assertIsInstance(plot.boxplot(self.pois), dict)
        self.assertGreater(len(plot.boxplot(self.gamma)), 0)
        self.assertGreater(len(plot.boxplot(self.exp)), 0)

if __name__ == "__main__":
    unittest.main()