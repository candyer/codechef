def mfreq(tmp,l,r,k):
	while r - l + 1 >= k:
		if tmp[r-1] >= k:
			return array[r-1]	
		r -= 1
	return -1

if __name__ == "__main__":
	n, m = map(int, raw_input().split())
	array = map(int, raw_input().split())
	tmp = [1]
	for i in range(1, n):
		if array[i] == array[i-1]:
			tmp.append(tmp[-1]+1)
		else:
			tmp.append(1)
	for _ in range(m):
		l, r, k = map(int, raw_input().split())
		print mfreq(tmp,l,r,k)
