import unittest
import pandas as pd
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

    def test_hits(self):
        pass
        
    def test_qqplot(self):
        pass
        
    def test_boxplot(self):
        pass

if __name__ == "__main__":
    unittest.main()