# https://www.codechef.com/JUNE16/problems/CHEARMY 

def solve(k):
    if k == 0: return '0'
    convert = {"0":"0", "1":"2", "2":"4", "3":"6", "4":"8"}
    res = []
    while k:
        res.append(convert[str(k % 5)])
        k = k / 5
    return "".join(res[::-1])
 
def chearmy():
    T = int(raw_input())
    for t in xrange(T):
        K = int(raw_input())
        print solve(K-1)
 
if __name__ == "__main__":
  chearmy()
