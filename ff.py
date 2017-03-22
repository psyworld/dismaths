#savthe.com/csproblems/ max_flow max_path
import queue
#Input----------------------------------------
constr = [list(map(int, input().split())) for i in f]
flow = [[0 for j in range(n)] for i in range(n)]
#Functions-------------------------------------
#generating random parent tree
def bfs(v, target):
	q = queue.Queue()
	used = [False for i in range(n)]                 
	mas = [0 for i in range(n)]
	q.put(v)
	used[v] = True
	while(not q.empty()):
		v = q.get()
		for i in range(n):
			if constr[v][i] != 0:
				if i == target:
					mas[v] = i
					return mas
				if used[i]:
					continue
				q.put(i)
				used[i] = True
				mas[v] = i
				break				 	
#creating path - array of vertices 
def patth():
	mas = bfs(0,1)
	if mas == None:
		return None
	path = []
	path.append(0)
	i = 0
	while (mas[i] != 1):
		path.append(mas[i])
		i = mas[i]
	path.append(1)
	return path
#minimal constraint of the path
def mconst(path):
	m = []                        
	for i in range(len(path)-1):
		m.append(constr[path[i]][path[i+1]])
	return min(m)
#----------------------------------------------
path = patth()
if path == None:
	minconst = 0
else:
	minconst = mconst(path)
	while(minconst != 0):
		for i in range(len(path)-1):
			a = path[i]
			b = path[i+1]
			flow[a][b] += minconst
			constr[a][b] -= minconst
			flow[b][a] -= minconst
			constr[b][a] += minconst
		path = patth()
		if path == None:
			minconst = 0
		else:	
			minconst = mconst(path)
W = 0
for i in range(n):
	W += flow[i][1]
#print('Мощность потока = ', W)