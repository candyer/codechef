# https://www.codechef.com/AUG18B/problems/SHKNUM


def f(n):
	count = 0
	while 2**count < n:
		count += 1
	return count

def solve(n):
	if n == 1: return 2
	if n == 2: return 1
	if n == 4: return 1
	count = f(n)
	remaining = n - 2**(count - 1)
	count1 = f(remaining)
	remaining1 = 2 ** count1 - remaining
	if count1 in [0, 1] : return 0
	if count - count1 == 1:
		return min(n - (2**(count - 1) + 2**(count1 - 1)), 2**count + 1 - n)
	else:
		return min(n - (2**(count - 1) + 2**(count1 - 1)), 2**(count - 1) + 2**count1 - n)

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		print solve(n)

assert solve(10**9)== 73741825 # 2**30 + 2**0 - 73741825
assert solve(127) == 2 # 2**7+2**0 - 2
assert solve(112) == 16 # 2**6 + 2**5 + 16 
assert solve(126) # 2**7 - 2
assert solve(129) == 0
assert solve(1) == 2
assert solve(15) == 2 # 2**4 + 2**0 - 2
assert solve(78) == 2 #2**6 + 2**4 - 2
assert solve(23) == 1 #2**4 + 2**3 - 1
assert solve(1536) == 0 #2**10 + 2**9
assert solve(10) == 0 #2**3 + 2**1
assert solve(22) == 2 #2**4 + 2**2 + 2
assert solve(4) == 1 #2**2 + 1
assert solve(1024) == 1 #2**10 + 1
