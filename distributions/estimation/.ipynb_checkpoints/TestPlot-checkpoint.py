import unittest
import pandas as pd
import mle

class TestMle(unittest.TestCase):
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
        print("Tearing Down the class")
    
    def setUp(self):
        print('setting up for the method')

    def tearDown(self):
        print("tearing down after the method")

    def test_hist(self):
        pass

    def test_qqplot(self):
        pass

    def test_boxplot(self):
        pass