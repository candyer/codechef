# https://www.codechef.com/APRIL17/problems/SIMDISH

def simdish(dish1, dish2):
	count = 0
	for d1 in dish1:
		if d1 in dish2:
			count += 1
			if count >= 2: return 'similar'
	return 'dissimilar'

if __name__ == "__main__":
	t = int(raw_input())
	for _ in range(t):
		dish1 = raw_input().split()
		dish2 = raw_input().split()
		print simdish(dish1, dish2)

# print simdish(['eggs', 'sugar', 'flour', 'salt'], ['sugar', 'eggs', 'milk', 'flour'])
# print simdish(['aa', 'ab', 'ac', 'ad'], ['ac', 'ad', 'ae', 'af'])
# print simdish(['cookies', 'sugar', 'grass', 'lemon'], ['lemon', 'meat', 'chili', 'wood'])
# print simdish(['one', 'two', 'three', 'four'], ['one', 'two', 'three', 'four'])
# print simdish(['gibberish', 'jibberish', 'lalalalala', 'popopopopo'], ['jibberisz', 'gibberisz', 'popopopopu', 'lalalalalu'])

