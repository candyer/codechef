# https://www.codechef.com/LOCJUL18/problems/COLCHEF

class DisjointSet():
	def __init__(self):
		self.leader = {}
		self.group = {}

	def add_edge(self, a, b):
		leadera = self.leader.get(a)
		leaderb = self.leader.get(b)
		if leadera is not None:
			if leaderb is not None:
				if leadera == leaderb: 
					return
				groupa = self.group[leadera]
				groupb = self.group[leaderb]
				if len(groupa) < len(groupb):
					a, leadera, groupa, b, leaderb, groupb = b, leaderb, groupb, a, leadera, groupa
				groupa |= groupb
				del self.group[leaderb]
				for k in groupb:
					self.leader[k] = leadera
			else:
				self.group[leadera].add(b)
				self.leader[b] = leadera
		else:
			if leaderb is not None:
				self.group[leaderb].add(a)
				self.leader[a] = leaderb
			else:
				self.leader[a] = self.leader[b] = a
				self.group[a] = set([a, b])

	def are_connected(self, a, b):
		if self.leader.get(a) == self.leader.get(b):
			return 'YES'
		return 'NO'


if __name__ == '__main__':
  n = int(raw_input())
  q = int(raw_input())
  connection = DisjointSet()
  for _ in range(q):
	  types, a, b = map(int, raw_input().split())
	  if types == 0:
		  connection.add_edge(a, b)
	  else:
		  print connection.are_connected(a, b)






