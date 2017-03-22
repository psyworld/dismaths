#savthe.com/csproblems/ max_flow max_path
import queue
#Input----------------------------------------
n = int(input())
constr = [list(map(int, input().split())) for i in range(n)]
flow = [[0 for j in range(n)] for i in range(n)]
#Functions-------------------------------------
#generating random parent tree
def bfs(v, target):
	q = queue.Queue()
	used = [False for i in range(n)]                 
	mas  = [0 for i in range(n)]
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
				mas[v]  = i
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
	k = 0 
	mini = 666 #:D
	for i in range(len(path)-1):
		m.append(constr[path[i]][path[i+1]])
		if m[i] <= mini:
			mini = m[i]
			k = i
		constr[path[k]][path[k+1]] = 0 #removing mini constraint edge 
	return mini
#--------------------------------------------
arr  = []
mc = []
path = patth()
while path != None:
	arr.append(path)
	mc.append(mconst(path))
	path = patth()
print(max(mc), '/n', *arr[mc.index(max(mc))])
