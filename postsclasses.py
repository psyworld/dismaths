def ftozh(mas0):
	mas1 = []
	mas1.append(mas0[0])
	for j in range(1, len(f)):
		for i in range(len(f)-1):
			mas0[i] += mas0[i+1] 
		mas1.append(mas0[0])
	return mas1

def mono(f):
	for i in range(len(f)-1):
		if i == 0 and f[0] == 0:
			continue
		for k in range(i+1, len(f)):
			if (i | k) == k and f[i] > f[k]:
				return 0
	return 1
#---------------------------------		
f = [int(i) for i in input()]
print(f)
#T0-------------------------------
if f[0] == 0:
	print('T0', end='\n')
#T1-------------------------------
if f[len(f)-1] == 1:
	print('T1', end='\n')
#S--------------------------------
k = 0
for i in range(len(f)//2):
	if f[i] == f[len(f)-1-i]:
		k = -1
		break
if k == 0:
	print('S', end='\n')
#L-------------------------------
zh = ftozh(f)
k = 0
for i in range(len(zh)):
	if i & (i-1) and zh[i] % 2 == 1:
		k = -1
		break
if k == 0:
	print('L', end='\n')
#M------------------------------
if mono(f) == 1:
	print('M')