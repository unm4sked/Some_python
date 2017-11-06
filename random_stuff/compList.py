

res = []
for x in 'mielonka':
	res.append(ord(x))

print(res)


res2 = list(map(ord,'mielonka'))
print(res2)

#------------------------------------------------------------------------------

z = [x ** 2 for x in range(10)]
print(z)

y = list(map((lambda x: x**2),range(10)))
print(y)


z = [x for x in range(10) if x % 2 == 0]
print(z)

#------------------------------------------------------------------------------


y = filter((lambda x: x % 2 == 0),range(10))
y = list(y) #trzeba rzutować
print(y)


res = []
for x in range(5):
	if x % 2 == 0:
		res.append(x)
print(res)

L = list(map((lambda x: x**2),filter((lambda x: x % 2 == 0),range(10))))
print(L)

#------------------------------------------------------------------------------

res  = [x + y for x in [0,1,2] for y in [100,200,300]]
print(res)

#------------------------------------------------------------------------------

res  = [x + y for x in 'jajko' for y  in 'JAJKO']
print(res)


#------------------------------------------------------------------------------
res = [(x,y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1 ]
print(res)

res = []
for x in range(5):
	if x % 2 == 0:
		for y in range(5):
			if y % 2 == 1:
				res.append((x,y))

print(res)