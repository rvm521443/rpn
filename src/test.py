import unittest
import rpn


class TestCalc(unittest.TestCase):
    def setUp(self):
        self.calc = rpn.Calc([float(x) for x in range(1, 5)])



class TestCalcOp1(TestCalc):
    def testClear(self):
        self.calc.op1(lambda _: 0)
        self.assertEqual([1.0, 2.0, 3.0, 0.0], self.calc.st)

    def testSquare(self):
        self.calc.op1(lambda x: x * x)
        self.assertEqual([1.0, 2.0, 3.0, 16.0], self.calc.st)


class TestCalcSp(TestCalc):
    def testClear(self):
        self.calc.op1(lambda _: 0)
        self.assertEqual([1.0, 2.0, 3.0, 0.0], self.calc.st)

    def testPut(self):
        self.calc.put(5.0)
        self.assertEqual(self.calc.st, [2.0, 3.0, 4.0, 5.0])

    def testPush(self):
        self.calc.push()
        self.assertEqual(self.calc.st, [2.0, 3.0, 4.0, 4.0])



if __name__ == '__main__':
    unittest.main()
