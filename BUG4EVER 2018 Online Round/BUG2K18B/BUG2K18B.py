# https://www.codechef.com/BUGE2018/problems/BUG2K18B

def solve(current, time_needed, expcted, delay):
	if current + time_needed <= expcted + delay:
		return 'Yes'
	return 'No'


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		curr_h, curr_m = map(int, raw_input().split(':'))
		current = curr_h * 60 + curr_m
		time_needed = int(raw_input())
		expcted_h, expcted_m = map(int, raw_input().split(':'))
		expcted = expcted_h * 60 + expcted_m
		delay = int(raw_input()) 
		print solve(current, time_needed, expcted, delay)


assert solve(470, 80, 540, 10) == 'Yes'
assert solve(470, 70, 540, -5) == 'No'