# https://www.codechef.com/SEPT18B/problems/MAGICHF

#######################
###### solution 1 #####
#######################
def solve(n, x, s, actions):
	boxes = [False] * (n + 1)
	boxes[x] = True
	res = x
	for a, b in actions:
		if boxes[a]:
			boxes[a], boxes[b] = boxes[b], boxes[a]
			res = b
		elif boxes[b]:
			boxes[a], boxes[b] = boxes[b], boxes[a]
			res = a
	return res


#######################
###### solution 2 #####
#######################
def solve(n, x, s, actions):
	res = x
	for a, b in actions:
		if a == res:
			res = b
		elif b == res:
			res = a
	return res


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, x, s = map(int, raw_input().split())
		actions = []
		for i in range(s):
			a, b = map(int, raw_input().split())
			actions.append((a, b))
		print solve(n, x, s, actions)


assert solve(5, 2, 4, [(4, 2), (3, 4), (3, 2), (1, 2)]) == 1
assert solve(5, 1, 3, [(1, 2), (3, 4), (2, 1)]) == 1






