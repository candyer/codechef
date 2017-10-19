# https://www.codechef.com/SEPT16/problems/LONGSEQ

def longseq(seq):
	if seq.count('1') == 1 or seq.count('0') == 1:
		return 'Yes'
	return 'No'

if __name__ == '__main__':
	T = int(raw_input())
	for _ in xrange(T):
		seq = raw_input()
		print longseq(seq)

# print longseq('101') #'Yes'
# print longseq('11') #'No'
# print longseq('1111111111111110') #'Yes'
