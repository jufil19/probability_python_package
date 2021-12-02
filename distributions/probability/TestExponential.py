import unittest
import math
from exponential import Exponential

class TestExponential(unittest.TestCase): 
    @classmethod
    def setUpClass(cls):
        print('setupclass')
    
    @classmethod
    def tearDownClass(cls):
        print('teardownclass')
    
    def setUp(self):
        self.exp1 = Exponential()
        print('setup')
    
    def tearDown(self):
        print('teardown')

    def test_pdf(self):
        self.assertRaises(ValueError, self.exp1.pdf, 3, -1)
        self.assertRaises(TypeError, self.exp1.pdf('0.5', 1))
        self.assertEqual(self.exp1.pdf(0, 1), 1)
        self.assertAlmostEqual(self.exp1.pdf(0.5, 5), 0.410425)
        self.assertAlmostEqual(self.exp1.pdf(1, 0.5), 0.3032653)

    def test_cdf(self):
        self.assertRaises(ValueError, self.exp1.cdf, 3, -1)
        self.assertRaises(TypeError, self.exp1.cdf('0.5', 1))
        self.assertEqual(self.exp1.cdf(0, 1), 0)
        self.assertAlmostEqual(self.exp1.cdf(1, 1), 0.6321206)
        self.assertAlmostEqual(self.exp1.cdf(0.4, 3), 0.6988058)

    def test_quantile(self):
        self.assertRaises(ValueError, self.exp1.quantile, 0.5, -1)
        self.assertRaises(TypeError, self.exp1.quantile('0.5', 1))
        self.assertEqual(self.exp1.quantile(0, 2), 0)
        self.assertEqual(self.exp1.quantile(1, 2), math.inf)
        self.assertAlmostEqual(self.exp1.quantile(0.5, 2), 0.3465736)
    

