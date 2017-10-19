
# https://www.codechef.com/LTIME51/problems/MATPAN

def solve(prices, text):
	res = 0
	miss = []
	for i in range(97, 123):
		if not chr(i) in text:
			res += prices[i - 97]
	return res

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		prices = map(int, raw_input().split())
		text = raw_input()
		print solve(prices, text)


# print solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26], 'abcdefghijklmopqrstuvwz') #63
# print solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26], 'thequickbrownfoxjumpsoverthelazydog')#0
