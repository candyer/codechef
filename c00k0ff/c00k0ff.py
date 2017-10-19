# https://www.codechef.com/LTIME52/problems/C00K0FF

def solve(n, difficulty):
	if 'cakewalk' not in difficulty:
		return 'No'
	elif 'simple' not in difficulty:
		return 'No'
	elif 'easy' not in difficulty:
		return 'No'
	elif 'easy-medium' not in difficulty and 'medium' not in difficulty:
		return 'No'
	elif 'medium-hard' not in difficulty and 'hard' not in difficulty:
		return 'No'
	return 'Yes'

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		difficulty = []
		for i in range(n):
			s = raw_input()
			difficulty.append(s)
		print solve(n, difficulty)


# print solve(5, ['easy', 'medium', 'medium-hard', 'simple', 'cakewalk']) #Yes
# print solve(7, ['simple', 'simple', 'medium', 'medium', 'easy-medium', 'cakewalk', 'easy']) #No
# print solve(7, ['cakewalk', 'simple', 'easy', 'easy-medium', 'medium', 'medium-hard', 'hard']) #Yes
