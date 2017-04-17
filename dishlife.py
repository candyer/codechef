# https://www.codechef.com/APRIL17/problems/DISHLIFE

from collections import defaultdict

def dishlife(n, k, array):
	d = defaultdict(lambda:0)
	for i in range(n):
		for ingredient in array[i]:
			d[ingredient] += 1
	if len(d) < k: return 'sad'

	for i in range(n):
		if all(d[ingredient] > 1 for ingredient in array[i]):
			return 'some'	
	return 'all'

if __name__ == "__main__":
	t = int(raw_input())
	for _ in range(t):
		n, k = map(int, raw_input().split())
		array = []
		for i in range(n):
			tmp = map(int, raw_input().split())
			array.append(tmp[1:])
		print dishlife(n, k, array)

# print dishlife(3, 5, [[3,5], [1,4], [1,2,5]]) # 'all'
# print dishlife(3, 5, [[3,5], [1,4], [1,2,3,5]]) # 'some'
# print dishlife(3, 5, [[3,5], [1,4], [1,2,3,4,5]]) # 'some'
# print dishlife(3, 4, [[1, 2, 3], [1, 3], [1, 2]]) # 'sad'
# print dishlife(2, 3, [[1, 2, 3], [1, 3]]) # 'some'
# print dishlife(2, 3, [[1, 3], [1, 2, 3]]) # 'some'
# print dishlife(2, 3, [[1, 2], [1, 3]]) # 'all'
# print dishlife(1, 2, [[1, 2]]) # 'all'


