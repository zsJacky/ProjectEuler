x = []
y = []

for i in range(1000):
	if i % 3 == 0:
		x.append(i)
	if i % 5 == 0:
		x.append(i)
	if i %15 == 0:
		y.append(i)

print sum(x) - sum(y)


