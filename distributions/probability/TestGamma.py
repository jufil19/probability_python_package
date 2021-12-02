import unittest
import math
from gamma import Gamma

class TestGamma(unittest.TestCase): 
    @classmethod
    def setUpClass(cls):
        print('setupclass')
    
    @classmethod
    def tearDownClass(cls):
        print('teardownclass')
    
    def setUp(self):
        self.gamma1 = Gamma()
        print('setup')
    
    def tearDown(self):
        print('teardown')

    def test_pdf(self):
        self.assertRaises(ValueError, self.gamma1.pdf, 3, 2, -1)
        self.assertRaises(TypeError, self.gamma1.pdf('0.5', 2, 1))
        self.assertEqual(self.gamma1.pdf(0, 1, 2), 2)
        self.assertAlmostEqual(self.gamma1.pdf(0.5, 2, 1), 0.3032653)
        self.assertAlmostEqual(self.gamma1.pdf(2, 2, 2), 0.1465251)

    def test_cdf(self):
        self.assertRaises(ValueError, self.gamma1.cdf, 3, -2, -1)
        self.assertRaises(TypeError, self.gamma1.cdf('0.5', 2, 1))
        self.assertEqual(self.gamma1.cdf(0, 1, 2), 0)
        self.assertAlmostEqual(self.gamma1.cdf(1, 1, 1), 0.6321206)
        self.assertAlmostEqual(self.gamma1.cdf(0.4, 2, 3), 0.3373727)

    def test_quantile(self):
        self.assertRaises(ValueError, self.gamma1.quantile, 0.5, 2, -1)
        self.assertRaises(TypeError, self.gamma1.quantile('0.5', 1, 2))
        self.assertEqual(self.gamma1.quantile(0, 2, 3), 0)
        self.assertEqual(self.gamma1.quantile(1, 2, 3), math.inf)
        self.assertAlmostEqual(self.gamma1.quantile(0.5, 2, 2), 0.8391735)
    

