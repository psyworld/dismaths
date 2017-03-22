import queue
#Functions-------------------------------------
#generating random path
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
					#creating path
					if mas == None:
						return None
					path = []
					path.append(v)
					i = 0
					while (mas[i] != target):
						path.append(mas[i])
						i = mas[i]
					path.append(target)
					return path
				if used[i]:
					continue
				q.put(i)
				used[i] = True
				mas[v] = i
				break				 	
#minimal constraint of the path
def mconst(path):
	m = []                        
	for i in range(len(path)-1):
		m.append(constr[path[i]][path[i+1]])
	return min(m)
#F.-F. algorithm 
def f_f(s, t):
	path = bfs(s, t)
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
			path = bfs(s,t)
			if path == None:
				minconst = 0
			else:	
				minconst = mconst(path)
	W = 0
	for i in range(n):
		W += flow[i][1]
	return W
#Input----------------------------------------
n = int(input())
m = int(input())
constr = [[0 for j in range(n+m+2)] for i in range(n+m+2)] #2 vertices for source and target
for i in range(n):
	s =  list(map(int, input().split()))
	for j in range(len(s)):
	constr[i][s[j]] = 1
for i in range(n): #source and left vrtices connecting
	constr[n+1][i] = 1
for i in range(m): #right vertices and target connecing
	constr[n+m+2-i][n+2] = 1 
n += m + 2
flow = [[0 for j in range(n)] for i in range(n)]
#----------------------------------------------------
#start F.-F. algorithm from source(n-2) to target(n-1)
print(f_f(n-2, n-1))