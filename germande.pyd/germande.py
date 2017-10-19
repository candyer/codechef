# https://www.codechef.com/FEB17/problems/GERMANDE

def germande(o1, o2, districts):
	n = o1 * o2
	districts += districts[:o2-1]
	running_sum = [0]
	for d in districts:
		running_sum.append(running_sum[-1] +  d)

	i = 0
	while i < o2:
		tmp1 = 0
		for j in range(i, n, o2):
			tmp2 = running_sum[j+o2] - running_sum[j]
			if tmp2 > o2 / 2:
				tmp1 += 1
		if tmp1 > o1/2:
			return 1
		i += 1
	return 0

if __name__ == "__main__":
	t = int(raw_input())
	for _ in range(t):
		o1, o2 = map(int, raw_input().split())
		districts = map(int, raw_input().split())
		print germande(o1, o2, districts)
