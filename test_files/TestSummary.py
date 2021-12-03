import unittest
import pandas as pd
from distributions.estimation import summary

class TestSummary(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    @classmethod
    def tearDownClass(cls):
        pass
    
    def setUp(self):
        self.l = [1,1,1,1,1,1,1,1,1,1,1]
        self.l2 = [1, 0.1, 1, 1, 1]
        self.l3 = [-1,1,1,1,1,1]

    def tearDown(self):
        pass

    def test_summary(self):
        self.assertEqual(summary.summary(self.l)["Mean"], 1)
        self.assertEqual(summary.summary(self.l)["Variance"], 0)
        self.assertEqual(summary.summary(self.l)["Min"], 1)
        self.assertEqual(summary.summary(self.l)["Max"], 1)
        self.assertRaises(TypeError, summary.summary, "Hello")
        

    def test_contains_all_ints(self):
        self.assertTrue(summary.contains_all_ints(self.l))
        self.assertFalse(summary.contains_all_ints(self.l2))
        self.assertTrue(summary.contains_all_ints(self.l3))
        self.assertFalse(summary.contains_all_ints(['hi', 'how', 'are', 'you']))
        self.assertFalse(summary.contains_all_ints("hello"))
        
    def test_is_non_negative(self):
        self.assertTrue(summary.is_non_negative(self.l))
        self.assertTrue(summary.is_non_negative(self.l2))
        self.assertFalse(summary.is_non_negative(self.l3))
        self.assertRaises(TypeError, summary.is_non_negative, ['hi', 'how', 'are', 'you'])
        self.assertRaises(TypeError, summary.is_non_negative, "hello")

if __name__ == "__main__":
    unittest.main()