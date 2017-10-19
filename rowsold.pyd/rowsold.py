# https://www.codechef.com/APRIL17/problems/ROWSOLD

def rowsold(array):
	res = 0
	index = 0
	n = len(array)
	if not '1' in array: return 0
	start = array.index('1')
	i = start
	while i < n:
		count = 0
		if array[i] == '0':
			index = i
			j = index
			while j < n:
				if array[j] == '0':
					count += 1
					j += 1
				else:
					break
			i = j
			tmp = (index - start) * (count + 1)
			res += tmp
			start += count
		i += 1
	return res

if __name__ == "__main__":
	t = int(raw_input())
	for _ in range(t):
		s = list(raw_input())
		print rowsold(s)

# print rowsold(['0', '1', '0', '1', '0', '1', '0', '1'])
# print rowsold(['1', '0', '1', '0', '1', '0', '1', '0'])
# print rowsold(['1', '0', '1', '0', '0']) == 8
# print rowsold(['1', '1', '0', '0', '0', '0', '1']) == 10
# print rowsold(['0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1']) == 0
# print rowsold(['0', '0', '1', '1', '1', '0', '1', '0', '0', '0', '1', '1', '0', '1', '0']) == 48
# print rowsold(['1', '1', '1', '1', '0', '0', '0', '0']) == 20


