# https://www.codechef.com/MARCH18A/problems/BIGSALE


from fractions import Fraction
def solve(n, recipes):
	res = 0
	for price, quantity, discount in recipes:
		rate = discount / Fraction(100.0)
		tmp = price * (rate ** 2)
		res += tmp * quantity
	return '{0:.6f}'.format(float(res))

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		recipes = []
		for i in range(n):
			price, quantity, discound = map(int, raw_input().split())
			recipes.append([price, quantity, discound])
		print solve(n, recipes)

# print solve(2, [[100, 5, 10], [100, 1, 50]])
# print solve(3, [[10, 10, 0], [79, 79, 79], [100, 1, 100]])
# print solve(3, [[10, 10, 1], [79, 79, 13], [100, 1, 27]])
# print solve(3, [[10, 10, 0], [79, 79, 0], [100, 1, 0]])

