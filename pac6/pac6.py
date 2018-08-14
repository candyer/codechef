# # https://www.codechef.com/problems/PAC6

# Dijkstra's algorithm


from collections import defaultdict
from heapq import heappop, heappush

def dijkstra(n, start, to, graph):
	cost = {i: float('inf') for i in range(1, n + 1)}
	cost[start] = 0
	visit = []
	heappush(visit, [0, start])

	while visit:
		start_cost, start_node = heappop(visit)

		for next_node, next_cost in graph[start_node]:
			if cost[start_node] + next_cost < cost[next_node]:
				cost[next_node] = cost[start_node] + next_cost
				heappush(visit, [cost[next_node], next_node])
	return cost[to]


if __name__ == '__main__':
	n, m, r, x, y = map(int, raw_input().split())
	graph = defaultdict(list)
	for _ in range(r):
		u, v, cost = map(int, raw_input().split())
		graph[u].append((v, cost))
		graph[v].append((u, cost))
	shortest_time_needed = dijkstra(n, x, y, graph)
	if shortest_time_needed <= m:
		print 'alive', shortest_time_needed
	else:
		print 'died'




