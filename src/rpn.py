import collections


class Calc:
    def __init__(self, it = None):
        it = it or [0.0] * 4
        self._st = collections.deque(it, maxlen=4)

    @property
    def st(self):
        return list(self._st)

    def op1(self, fn):
        st = self._st
        st.append(fn(st.pop()))

    def put(self, val):
        self._st.append(val)
    
    def push(self):
        self._st.append(self._st[-1])

    def __repr__(self):
        return f'Calc({self.st})'

