# https://www.codechef.com/problems/CIELAB

def solve(a,b):
    """1 <= b < a <= 10000 """
    diff = str(a-b)
    if diff[-1] == "9": 
        return (a-b) - 1
    else:
        return (a-b) + 1

def cielab():
    import sys
    for line in sys.stdin:
        a,b = map(int,(line.split()))
        print solve(a,b)

if __name__ == "__main__":
    cielab()