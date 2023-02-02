import unittest
import rpn

class TestCalcOp1(unittest.TestCase):
    def setUp(self):
        self.calc = rpn.Calc([float(x) for x in range(1, 5)])

    def testClear(self):
        self.calc.op1(lambda _: 0)
        self.assertEqual([1.0, 2.0, 3.0, 0.0], self.calc.st)

    def testSquare(self):
        self.calc.op1(lambda x: x * x)
        self.assertEqual([1.0, 2.0, 3.0, 16.0], self.calc.st)

if __name__ == '__main__':
    unittest.main()
