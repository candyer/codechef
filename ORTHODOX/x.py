
from math import log2 
def givesum(A) : 
	n = len(A)
	totalSubarrays = n * (n + 1) // 2
	s = 0
	for i in range(int(log2(max(A))) + 1): 
		vec = [] 
		sum = 0
		print('--------------------i:', i, vec, sum)
		for j in range(n): 
			a = A[j] >> i 
			if (not(a & 1)): 
				vec.append(j) 
		print('----------j:', j, a, vec)
		print()
		cntSubarrNotSet = 0
		cnt = 1
		for j in range(1, len(vec)): 
			if (vec[j] - vec[j - 1] == 1): 
				cnt += 1
			else: 
				cntSubarrNotSet += cnt * (cnt + 1) // 2
				cnt = 1
		cntSubarrNotSet += cnt * (cnt + 1) // 2
		if len(vec) == 0: 
			cntSubarrNotSet = 0	
		cntSubarrIthSet = totalSubarrays - cntSubarrNotSet 
		s += cntSubarrIthSet * pow(2, i) 
	return s 

print(givesum([1, 2, 3, 4, 5])) 

