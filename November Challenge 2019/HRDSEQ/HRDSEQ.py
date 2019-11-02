# https://www.codechef.com/NOV19B/problems/HRDSEQ


def seq():
	arr = [0]
	x = 0
	for i in range(130):
		j = i - 1
		while j >= 0:
			if arr[j] == x:
				arr.append(i - j)
				x = i - j
				break
			j -= 1
		if j == -1:
			arr.append(0)
			x = 0
	return arr	

def solve(arr, n):
	tmp = arr[n - 1]
	return arr[:n].count(tmp)

if __name__ == '__main__':
	t = int(raw_input())
	sequence = seq()
	for _ in range(t):
		n = int(raw_input())
		print solve(sequence, n)