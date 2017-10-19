# https://www.codechef.com/COOK81/problems/CANDY123

# def candy123(a, b):
# 	i = 1
# 	count1 = 0
# 	while True:
# 		if a - i >= 0:
# 			count1 += 1
# 			a -= i
# 		else: 
# 			break
# 		i += 2

# 	j = 2
# 	count2 = 0
# 	while True:
# 		if b - j >= 0:
# 			count2 += 1
# 			b -= j
# 		else: 
# 			break
# 		j += 2
# 	if count1 > count2: return 'Limak'
# 	return 'Bob'

def candy123(a, b):
	turn = 1 
	while True:
		#In this turn the person should eat exactly 'turn' candies.
		#if 'turn' is odd, then it is Limak's turn, otherwise Bob's.
		if turn % 2 == 1:
			a -= turn;
			if a < 0:
				return "Bob"; #limak can't eat these 'turn' candies, so Bob will win.
		else:
			b -= turn;
			if b < 0:
				return "Limak"; #Bob can't eat these 'turn' candies, so Limak will win.
		turn += 1;

if __name__ == '__main__':
	t = int(raw_input())
	for i in range(1,t+1):
		a, b = map(int, raw_input().split())
		print candy123(a, b)

# print candy123(3, 2) #'Bob'
# print candy123(4, 2) #'Limak'
# print candy123(1, 1) #'Limak'
# print candy123(1, 2) #'Bob'
# print candy123(1, 3) #'Bob'
# print candy123(9, 3) #'Limak'
# print candy123(9, 11) #'Limak'
# print candy123(9, 12) #'Bob'
# print candy123(9, 1000) #'Bob'
# print candy123(8, 11) #'Bob'
