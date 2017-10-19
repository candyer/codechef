# https://www.codechef.com/LOCJUL16/problems/FORALN


def solve(array):
	count_ka = count_ki = 0
	for a in array:
		if a[-2:] == 'ka':
			count_ka += 1
		elif a[-2:] =='ki':
			count_ki += 1
	return min(count_ka, count_ki)

def foraln(N, array):
	tmp = {}
	for a in array: 
		if a[-2:]== 'ki' or a[-2:]== 'ka':
			if not a[:2] in tmp:
				tmp[a[:2]] = [a]
			else:
				tmp[a[:2]].append(a)
	count = 0
	for val in tmp.values():
		if len(val) > 1:
			count += solve(val)
	return count

if __name__ == "__main__":
	"""
	1 <= N <= 1000
	3 <= Length of the name <= 100
	"""
	N = int(raw_input())
	array = raw_input().split()
	print foraln(N, array)
