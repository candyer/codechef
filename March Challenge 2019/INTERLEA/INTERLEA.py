# https://www.codechef.com/MARCH19A/problems/INTERLEA


'''
N=10000
|Si|=100
All the characters in Si are from the set {'0', '1', ..., '9'}
'''

from collections import deque, defaultdict
def solve(n, deq):
    next_pool = defaultdict(list)
    for i, nums in enumerate(deq):
        next_pool[nums.popleft()].append(i + 1)

    cur = min(next_pool)
    positions = []
    count = 0
    while count < n * 100:
        tmp = next_pool[cur]
        for pos in next_pool[cur]:
            count += 1
        positions.extend(tmp)
        next_pool.pop(cur)

        for pos in tmp:
            if deq[pos - 1]:
                next_pool[deq[pos - 1].popleft()].append(pos)
                
        diff1 = 100
        next_curr = 0
        for key in next_pool:
            if abs(cur - key) < diff1:
                diff1 = abs(cur - key)
                next_curr = key
        cur = next_curr
    return ' '.join(map(str, positions))


if __name__ == '__main__':
    n = int(raw_input())
    deq = []
    for _ in range(n):
        tmp = deque(map(int, raw_input()))
        deq.append(tmp)
    print solve(n, deq)



# print solve(3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])# == '1 1 1 2 2 2 3 3 3'
# print solve(3, [[3, 5, 7], [2, 6, 3], [1, 8, 1]])# == '1 2 3 1 2 1 3 2 3'
# print solve(3, [[6, 5, 7], [9, 8, 3], [7, 8, 1]])# == '1 1 3 1 3 2 2 2 3'

# from random import randint as r
# n = 10000
# s = []
# for _ in range(n):
#   sub = []
#   for i in range(100):
#       sub.append(str(r(0, 9)))
#   s.append(''.join(sub))
# print n
# print  '\n'.join(s)







































