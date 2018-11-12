# https://www.codechef.com/NOV18B/problems/HMAPPY1


######### small input ##########
# def longest_seq_1(n, array, k):
# 	one = 0
# 	maxi = 0
# 	for num in array + [0]:
# 		if num == 1:
# 			one += 1
# 		else:
# 			maxi = max(maxi, one)
# 			one = 0
# 	return str(min(maxi, k))


# def solve(n, q, k, array, s):
# 	'''
# 	1 <= K <= N <= 10^5
# 	1 <= Q <= 3*10^5
# 	0 <= Ai <= 1 for each valid i
# 	S contains only characters '?' and '!'
# 	'''		
# 	res = []
# 	for query in s:
# 		if query == '?':
# 			res.append(longest_seq_1(n, array, k))
# 		else:
# 			print array
# 			array = [array[-1]] + array[:-1]

# 	return '\n'.join(res)


# if __name__ == '__main__':
# 	n, q, k = map(int, raw_input().split())
# 	array = map(int, raw_input().split())
# 	s = raw_input()
# 	print solve(n, q, k, array, s)



######### large input ##########
def find_biggest_one_blocks(n, array):
	# given an array of '1's and '0's, and it's length
	# generate all the '1's block start and end index with length.  (length of longest block of one, start, end)
	blocks = []
	count = 0
	pre, cur = -1, 0
	for num in array + [0]:
		if num == '1':
			if pre == -1:
				pre = cur
		elif pre != -1:
			blocks.append([cur - pre, pre, cur])
			count += 1
			pre = -1
		cur += 1

	# merge first and last block together if the first and last elem are both '1'
	if count == 0:
		return []
	elif count >= 2:
		begin, end = blocks[0], blocks[-1]
		if array[0] == array[-1] == '1':
			tmp = [end[0] + begin[0], (n - end[1]) * (-1), begin[2]]
			blocks = blocks[1:-1] + [tmp]

	# sort blocks by decending order, and chose the first two elem if length > 2, else just the biggest one.
	blocks.sort(reverse=True)
	if len(blocks) >= 2:
		return blocks[:2]
	return blocks

def rotate(n, blocks, count_rotate):
	m = len(blocks)
	if count_rotate == 0 or m == 0:
		return blocks
	for i in range(m):
		length, begin, end = blocks[i]
		begin += count_rotate
		end += count_rotate
		if end > n:
			end -= n
			begin -= n
		blocks[i] = (length, begin, end)
	return blocks

def get_longest(block):
	length, begin, end = block
	if begin < 0:
		return max(abs(begin), length + begin)
	return length

def solve(blocks):
	m = len(blocks)
	if m == 0:
		return 0
	if m == 1:
		return get_longest(blocks[0])
	else:
		first, second = blocks
		return max(get_longest(first), get_longest(second))


if __name__ == '__main__':
	n, q, k = map(int, raw_input().split())
	array = raw_input().split()
	s = raw_input()
	blocks = find_biggest_one_blocks(n, array)
	count_rotate = 0
	for query in s:
		if query == '?': 
			count_rotate %= n
			blocks = rotate(n, blocks, count_rotate)
			print min(k, solve(blocks))
			count_rotate = 0
		else:
			count_rotate += 1













