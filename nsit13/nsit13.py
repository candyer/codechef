# https://www.codechef.com/problems/NSIT13

def nsit13():
    for test in range(10):
        count = set()
        for _ in range(10):
            t = int(raw_input())
            count.add(t%42)
        print len(count)

if __name__ == "__main__":
    nsit13()
