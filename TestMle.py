import unittest
import pandas as pd
from distributions.estimation import mle

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
        pass
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_readData(self):
        self.assertEqual(mle.readData(self.__class__.expfile), self.__class__.exp)
        self.assertIsInstance(mle.readData(self.__class__.expfile), list)
        self.assertRaises(FileNotFoundError, mle.readData, 'notafile.csv')
        self.assertRaises(ValueError, mle.readData, 'hasnegs.csv')
        self.assertRaises(ValueError, mle.readData, 'mulcols.csv')

    def test_setDistribution(self):
        self.assertEqual(mle.setDistribution('gamma'), 2)
        self.assertEqual(mle.setDistribution('poisson'), 3)
        self.assertEqual(mle.setDistribution('exponential'), 1)
        self.assertRaises(ValueError, mle.setDistribution, 'normal')
        self.assertRaises(ValueError, mle.setDistribution, 'Gamma')
        
    def test_calculate_mle(self):
        self.assertAlmostEqual(mle.calculate_mle('exponential', self.__class__.exp), 4, 0)
        self.assertAlmostEqual(mle.calculate_mle('poisson', self.__class__.pois), 4, 0)
        self.assertAlmostEqual(mle.calculate_mle('gamma', self.__class__.gamma)[0], 2, 0)
        self.assertAlmostEqual(mle.calculate_mle('gamma', self.__class__.gamma)[1], 4, 0)
        self.assertRaises(ValueError, mle.calculate_mle, 'poisson', [1.2,3.4,5.3])

if __name__ == "__main__":
    unittest.main()