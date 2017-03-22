import queue
#-----------------------------
print('Put num of vertices')
n = int(input())
print('Put num of edges')
m = int(input())
flow = [[0 for j in range(n)] for i in range(n)]
constr = [[0 for j in range(n)] for i in range(n)]
for i in range(m):
	print('From ')
	fr = int(input())
	print('To ')
	to = int(input())
	print('flow = ')
	flow[fr][to] = int(input())
	print('constraint = ')
	constr[fr][to] = int(input())
#-------------------------------
print(flow, end= '\n')
print(constr, end= '\n')

constr = [[constr[i][j]-flow[i][j] for j in range(n)] for i in range(n)]
used = [False for i in range(n)]
q = queue.Queue()

print(constr, end= '\n')

def bfs(v, target): 
	q.put(v)
	used[v] = True
	while(not q.empty()):
		v = q.get()
		for i in range(n):
			if constr[v][i] != 0:
				if i == target:
					return True
				if used[i]:
					continue
				q.put(i)
				used[i] = True

if bfs(0, 1):
	print('it is not max flow')
else:
	print('it is max flow')