# https://www.codechef.com/MARCH18B/problems/CHEGLOVE


def solve(n, fingers, glove):
	front = False
	back = False
	if all(f <= g for f, g in zip(fingers, glove)):
		front = True
	flipped_golve = glove[::-1]
	if all(f <= g for f, g in zip(fingers, flipped_golve)):
		back = True
	if front and back:
		return 'both'
	elif front:
		return 'front'
	elif back:
		return 'back'
	return 'none'

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		fingers = map(int, raw_input().split())
		glove = map(int, raw_input().split())
		print solve(n, fingers, glove)

# assert solve(3, [1, 2, 3], [2, 3, 4]) #'front'
# assert solve(3, [1, 2, 1], [1, 2, 1]) #'both'
# assert solve(3, [3, 2, 1], [1, 2, 3]) #'back'
# assert solve(4, [1, 3, 2, 4], [1, 2, 3, 5]) #'none'

