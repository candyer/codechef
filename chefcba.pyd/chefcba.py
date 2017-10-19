# https://www.codechef.com/problems/CHEFCBA

def solve(array):
	'''1 <= a, b, c, d <= 1000'''
	tmp = sorted(array)
	# line 7 is working, but I don't recommand 'float"
	# if float(tmp[0]) / tmp[1] == float(tmp[2]) / tmp[3]:
	# line 9 is better than line 7
	if tmp[0] * tmp[3] == tmp[1] * tmp[2]:
		return 'Possible'
	return 'Impossible'

def chefcba():
	array = map(int, raw_input().split())
	print solve(array)

if __name__ == "__main__":
	chefcba()
