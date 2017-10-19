# https://www.codechef.com/problems/CHEFRRUN

def chefrrun(N, tastyness):
    count = [True] * N
    res = 0
    for i in xrange(N):
        if count[i]:
            nexts = (i + tastyness[i] + 1) % N
            tmp = []
            while count[nexts]:
                tmp.append(nexts)
                count[nexts] = False
                nexts += tastyness[nexts] + 1
                nexts %=  N
            if nexts in tmp:    
                res += len(tmp) - tmp.index(nexts)
    return res
 
if __name__ == "__main__":
    T = int(raw_input())
    for _ in xrange(T):
        N = int(raw_input())
        tastyness = map(int,raw_input().split())
        print chefrrun(N, tastyness) 
