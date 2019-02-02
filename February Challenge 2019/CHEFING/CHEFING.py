# https://www.codechef.com/FEB19B/problems/CHEFING

'''
1 <= T <= 1,000
1 <= N <= 1,000
1 <= |Si| <= 200 for each valid i
S1, S2, ..., SN contain only lowercase English letters
The sum of length of strings over all test cases <= 3500000
'''

from collections import defaultdict
def solve(n, dishes):
	ingredients = defaultdict(int)
	for dish in dishes:
		for ingredient in dish:
			ingredients[ingredient] += 1
	res = 0
	for num in ingredients.values():
		if num == n:
			res += 1
	return res

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		dishes = []
		for i in range(n):
			dish = set(raw_input())
			dishes.append(dish)
		print solve(n, dishes)



		