# https://www.codechef.com/COOK80/problems/ROBOTG

def robotg(n, m, s):
    a, b = [0], [0]
    x = y = 0
    for i in s:
        if i == 'U':
            x -= 1
            a.append(x)
        elif i == 'D':
            x += 1
            a.append(x)
        elif i == 'L':
            y -= 1
            b.append(y)
        elif i == 'R':
            y += 1
            b.append(y)

    row = max(a) - min(a) + 1
    col = max(b) - min(b) + 1
    if row > n or col > m: 
        return 'unsafe'
    else:
        return 'safe'

if __name__ == "__main__":
	t = int(raw_input())
	for _ in range(t):
		n, m = map(int, raw_input().split())
		s = raw_input()
		print robotg(n, m, s)

# print robotg1(1, 1, 'R') #unsafe
# print robotg1(2, 3, 'LLRU') #safe
# print robotg1(3, 2, 'LLRU') #unsafe
# print robotg1(4, 3, 'ULURUDRDLD') #safe
# print robotg1(3, 6, 'RURUR') #safe
