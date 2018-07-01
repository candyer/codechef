# https://www.codechef.com/problems/SUMPOWER


#######################
### brute force TLE ###
#######################
def hamming_distance(s1, s2):
	count = 0
	for c1, c2 in zip(s1, s2):
		if c1 != c2:
			count += 1
	return count

def solve(n, k, s):
	res = 0
	i = k
	sub_string = s[: k]
	while i < n:
		new_sub = sub_string[1:] + s[i]
		res += hamming_distance(sub_string, new_sub)
		sub_string = new_sub
		i += 1
	return res



#######################
######### AC ##########
#######################
def solve(n, k, s):
	diff = [0] * n
	for i in range(1, n):
		if s[i] != s[i - 1]:
			diff[i] = 1
	
	for i in range(n):
		diff[i] += diff[i - 1]

	res = 0
	for i in range(k):
		res += diff[i + n - k] - diff[i]
	return res

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, k = map(int, raw_input().split())
		s = raw_input()
		print solve(n, k, s)

assert solve(6, 3, 'aabbcc') == 4
assert solve(5, 2, 'abccc') == 3
assert solve(4, 3, 'aabb') == 1
