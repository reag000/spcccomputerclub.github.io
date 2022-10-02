from glob import glob


t = [input() for i in range(3)]
c1 = c2 = 0
def f(z):
    global c1, c2
    if z == 1: c1 += 1
    elif z == 2: c2 += 1
for s in t:
    f(len(set([c for c in s])))
for i in range(3):
    f(len(set([t[j][i] for j in range(3)])))
f(len(set([t[0][0], t[1][1], t[2][2]])))
f(len(set([t[0][2], t[1][1], t[2][0]])))
print(c1, c2, sep='\n')
