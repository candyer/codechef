# https://www.codechef.com/COOK101B/problems/YVNUM



def solve(num, array):
	mod = 10**9 + 7
	n = len(num)
	res = 0
	prefix = [0]
	suffix = [0]
	for i in range(1, n + 1):
		prefix.append((prefix[i - 1] * 10 + int(num[i - 1])) % mod)
		suffix.append((int(num[n - i]) * array[i - 1] + suffix[i - 1]) % mod)

	power = [1]
	for i in range(1, n):
		power.append((power[i - 1] * array[n]) % mod)

	for i in range(n):
		tmp = ((suffix[n - i] * array[i] + prefix[i]) * power[n - 1 - i]) % mod
		res += tmp 
		res %= mod
	return res

if __name__ == '__main__':
	mod = 10**9 + 7
	array = [1]
	for i in range(1, 10**5 + 1):
		array.append((array[i - 1] * 10) % mod)

	t = int(raw_input())
	for _ in range(t):
		num = raw_input()
		print solve(num, array)



# assert solve('123') == 123231312
# assert solve('98752192634') == 556196341

