# https://www.codechef.com/problems/FSQRT

import math
def fsqrt():
    T = int(raw_input())
    for t in xrange(T):
        N = int(raw_input())
        print int(math.sqrt(N))
if __name__ == "__main__":
    fsqrt()
