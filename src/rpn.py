import collections


class Calc:
    def __init__(self, st = None):
        it = st or [0.0] * 4
        self._st = collections.deque(it, maxlen=4)

    @property
    def st(self):
        return list(self._st)

    def op1(self, fn):
        self._st[-1] = fn(self._st[-1])

    def put(self, val):
        self._st.append(val)
    
    def push(self):
        self._st.append(self._st[-1])

