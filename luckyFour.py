# https://www.codechef.com/problems/LUCKFOUR

def solve(s):
    count = 0
    for c in s:
        if c == "4":
            count += 1
    return count
 
def four():
    T = int(raw_input())
    for i in range(T):
        num = raw_input()
        print solve(num)
 
if __name__ == '__main__':
    four() 