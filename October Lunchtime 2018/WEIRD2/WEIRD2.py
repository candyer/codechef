# https://www.codechef.com/LTIME65B/problems/WEIRD2


# from collections import Counter as c
# def solve(n, array):
# 	d = c(array)
# 	count = 0
# 	key = d.keys()
# 	m = len(key)

# 	for i in range(m):
# 		if d[key[i]] >= key[i]:
# 			count += 1
# 		for j in range(i + 1, m):
# 			if d[key[i]] >= key[j] and d[key[j]] >= key[i]:
# 				count += 2
# 	return count



from collections import Counter as c
def solve(n, array):
	d = c(array)
	count = 0
	for num in d:
		for i in range(1, d[num] + 1):
			if i in d and d[i] >= num:
				count += 1	
	return count

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		array = map(int, raw_input().split())
		print solve(n, array)


assert solve(5, [1, 2, 3, 4, 5]) == 1
assert solve(5, [1, 1, 2, 2, 3]) == 4
assert solve(5, [3, 3, 2, 2, 2]) == 3




