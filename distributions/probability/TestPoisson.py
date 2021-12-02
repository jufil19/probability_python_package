import unittest
import math
from poisson import Poisson

class TestPoisson(unittest.TestCase): 
    @classmethod
    def setUpClass(cls):
        print('setupclass')
    
    @classmethod
    def tearDownClass(cls):
        print('teardownclass')
    
    def setUp(self):
        self.pois1 = Poisson()
        print('setup')
    
    def tearDown(self):
        print('teardown')

    def test_pdf(self):
        self.assertRaises(ValueError, self.pois1.pdf, 3, -1)
        self.assertRaises(TypeError, self.pois1.pdf('0.5', 1))
        self.assertEqual(self.pois1.pdf(0, 0), 1)
        self.assertEqual(self.pois1.pdf(0.5, 5), 0) #non-integer value
        self.assertAlmostEqual(self.pois1.pdf(1, 0.5), 0.3032653)

    def test_cdf(self):
        self.assertRaises(ValueError, self.pois1.cdf, 3, -1)
        self.assertRaises(TypeError, self.pois1.cdf(0.5, '1'))
        self.assertAlmostEqual(self.pois1.cdf(0, 1), 0.3678794)
        self.assertAlmostEqual(self.pois1.cdf(2.5, 2), 0.6766764)
        self.assertEqual(self.pois1.cdf(0, 0), 1)

    def test_quantile(self):
        self.assertRaises(ValueError, self.pois1.quantile, 0.5, -1)
        self.assertRaises(TypeError, self.pois1.quantile('0.5', 1))
        self.assertEqual(self.pois1.quantile(0.1, 2), 0)
        self.assertEqual(self.pois1.quantile(1, 2), math.inf)
        self.assertEqual(self.pois1.quantile(0.5, 2), 2)
    

