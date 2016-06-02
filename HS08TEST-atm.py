# https://www.codechef.com/problems/HS08TEST

def solve(withdraw, balance):
    if withdraw % 5 == 0 and withdraw + 0.50 < balance:
        return "%.2f" % (balance - withdraw - 0.50)
    return "%.2f" % balance

def ATM():
    a, b = raw_input().split()
    withdraw, balance =int(a), float(b)
    print solve(withdraw, balance)

if __name__ == '__main__':
    ATM()

