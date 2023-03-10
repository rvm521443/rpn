import unittest
import rpn
import operator


class TestCalc(unittest.TestCase):
    def setUp(self):
        self.calc = rpn.Calc([float(x) for x in range(1, 5)])


class TestCalcOp1(TestCalc):
    def testSquare(self):
        self.calc.op1(lambda x: x * x)
        self.assertEqual([1.0, 2.0, 3.0, 16.0], self.calc.st)


class TestCalcOp2(TestCalc):
    def testAdd(self):
        self.calc.op2(operator.add)
        self.assertEqual([2.0, 3.0, 4.0, 7.0], self.calc.st)

    def testSub(self):
        self.calc.op2(operator.sub)
        self.assertEqual([2.0, 3.0, 4.0, -1.0], self.calc.st)

class TestCalcSp(TestCalc):

    def testPut(self):
        self.calc.put(5.0)
        self.assertEqual(self.calc.st, [2.0, 3.0, 4.0, 5.0])

    def testPush(self):
        self.calc.push()
        self.assertEqual(self.calc.st, [2.0, 3.0, 4.0, 4.0])

    def testSwapXY(self):
        self.calc.swap_xy()
        self.assertEqual([1.0, 2.0, 4.0, 3.0], self.calc.st)


if __name__ == '__main__':
    unittest.main()
