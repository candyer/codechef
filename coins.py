# https://www.codechef.com/problems/COINS

# solutoion 1 too slow 
# def solve(coin):
#     if coin == 0: return 0
#     exchange = solve(coin/2) + solve(coin/3) + solve(coin/4)
#     if coin > exchange:
#         return coin 
#     else:
#         return exchange


def solve(coin2):
    d = {0:0}

    def exchange(coin):
        if coin in d:
            return d[coin]
        else:
            d[coin] = max(coin, exchange(coin/2) + exchange(coin/3) + exchange(coin/4))
            return d[coin]
    return exchange(coin2)

def coins():
    import sys
    for coin in sys.stdin:
        if coin[-1] == "\n":
            print solve(int(coin[:-1]))
        else:
            print solve(int(coin))

if __name__ == '__main__':
    coins()

