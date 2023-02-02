class Calc:
    def __init__(self, st = None):
        self._st = st or [0.0, 0.0, 0.0, 0.0]

    @property
    def st(self):
        return self._st

    def op1(self, fn):
        self._st[-1] = fn(self._st[-1])

