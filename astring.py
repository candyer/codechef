
import heapq
def solve(s,k):
    #1
    # import itertools
    # return ''.join(min(itertools.combinations(s,k)))

    #2
    # res = []
    # n = len(s)
    # j = 0
    # while k > 0:
    #     sub = s[j:n-k+1]
    #     res.append(min(sub))
    #     index_min = sub.index(min(sub))
    #     j += index_min+1
    #     k -= 1
    # return "".join(res)

    #3-1
    # res = []
    # start_index = -1
    # end_index = len(s) - k
    # h = [(y, x) for x, y in enumerate(s[:end_index])]
    # heapq.heapify(h)

    # for _ in range(k):
    #     # enlarge the window of one toward the right
    #     heapq.heappush(h, (s[end_index], end_index))
    #     end_index += 1
    #     # select the smallest val within [start_index : end_index]
    #     while True:
    #         val, ind = heapq.heappop(h)
    #         if ind > start_index: break


    #     # ind = float('-inf')
    #     # while ind < start_index:
    #     #     val, ind = heapq.heappop(h)
    #     # pick this letter and shorter the left side of the window
    #     res.append(val)
    #     start_index = ind

    # return ''.join(res)

    #3-2
    # res = []
    # start_index = -1
    # end_index = len(s) - k
    # #choose the staring window
    # h = [(y, x) for x, y in enumerate(s[:end_index])]
    # heapq.heapify(h)

    # for _ in range(k):
    #     # enlarge the window by increamenting one (character, pos_of_haracter) from right
    #     heapq.heappush(h, (s[end_index], end_index))
    #     end_index += 1
    #     # get the min from s[start_index : end_index] by using heappop (O(logN)) 
    #     while True:
    #         val, ind = heapq.heappop(h)
    #         if ind > start_index: break
    #     # save the min, shorten the window
    #     res.append(val)
    #     start_index = ind
        
    # return ''.join(res)

print solve('bwzxswedlihefbdsdewlnwelknxkwlxlaadfghjkljhgflkjhgafghjkoiuytfghjkloiuygfkliuhglkjhgdctsgehdydcdsdsd', 100) 
print solve('bacb', 2) #'ab'
print solve('babdcefaghja',5) #'aagha'
assert solve('abdcefghj',5) == 'abcef'
assert solve('abcdef', 2) == 'ab'
assert solve('abcdef', 0) == ''
assert solve('def', 3) == 'def'


def astring():
    T = int(raw_input())
    for t in range(T):
        s = raw_input()
        k = int(raw_input())
        print solve(s,k)

# if __name__ == "__main__":
#   astring()


