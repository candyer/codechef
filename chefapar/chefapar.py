# https://www.codechef.com/FEB17/problems/CHEFAPAR

def chefapar(n, status):
	if 0 in status:
		start_of_0 = status.index(0)
	else:
		return 0
	count_of_0 = status.count(0)
	i = start_of_0
	j = i + 1
	count = 0
	while i < n and j < n:
		while status[i] == 0:
			if status[j] == 1:
				status[i], status[j] = 1, 0
				i += 1
				count += 1
			else:
				j += 1
				if j == n: break
	return count_of_0 * 1100 + count * 100

if __name__ == "__main__":
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		status = map(int, raw_input().split())
		print chefapar(n, status)



# print chefapar(2, [1,1]) #0
# print chefapar(2,[0,0]) #2200
# print chefapar(3,[0,1,0]) #2300
# print chefapar(2,[0,1]) #1200
# print chefapar(6, [0,1,1,0,0,1]) #3600
# print chefapar(8,[1,1,0,0,1,0,1,1]) #3600
# print chefapar(10,[1,0,0,0,1,1,1,1,1,1]) #3900
# print chefapar(9,[0,0,1,1,1,0,1,0,0]) #5900
# print chefapar(6, [0,1,1,0,0,1]) #3600
# print chefapar(8, [1,1,1,1,1,0,1,0]) #2300
