# https://www.codechef.com/problems/TIDRICE

def tidrice():
    T = int(raw_input())
    for t in xrange(T):
        N = int(raw_input())
        votes = {}
        for n in xrange(N):
            user, score = raw_input().split()
            if score == '+':
                votes[user] = 1
            else:
                votes[user] = -1
        print sum(votes.values())

if __name__ == "__main__":
    tidrice()
