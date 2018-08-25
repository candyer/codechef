# https://www.codechef.com/BUGE2018/problems/BUG2K18C

from collections import Counter as c
def solve(s1, s2):
	d1, d2 = c(s1), c(s2)
	for key, val in d1.items():
		if d2[key] < val:
			return 'No'
	return 'Yes'


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		s1, s2 = raw_input().split()
		print solve(s1, s2)


assert solve('dare', 'darlene') == 'Yes'
assert solve('MrRobot', 'BootMrR') == 'No'
assert solve('Hello4riend', '4444eeediHlol89d7r5n') == 'Yes'
assert solve('2TheDARKARMY', 'DAARRKYMThen482') == 'Yes'
