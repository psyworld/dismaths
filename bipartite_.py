import queue
#----------------------------------------
n = int(input()) #num of vertices
mas = [list(map(int, input().split())) for i in range(n)]
set = [-1 for i in range(n)] #set of labels on the vertices (0 or 1)
q = queue.Queue()
def bfs(v): 
	q.put(v)
	set[v] = 0
	ch = 0
	while(not q.empty()):
		v = q.get()
		ch = set[v]
		for i in range(n):
			if mas[v][i] != 0:
				if set[i] == -1:
					set[i] = (ch + 1) % 2 
					q.put(i)
				elif set[v] == set[i]:
					return "NO"					
	return "YES"
print(bfs(0))