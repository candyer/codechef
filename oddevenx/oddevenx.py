def oddevenx():
	N = int(raw_input())
	seq = map(int, raw_input().split())
	odd = even = 0
	for s in seq:
		if s % 2 == 0:
			odd += 1
		else:
			even += 1
	print abs(odd - even)

if __name__ == '__main__':
	oddevenx()
