n = int(input())
ncows = []
ecows = []
for i in range(n):
    dir, x, y = input().split()
    if dir == 'N':
        ncows.append((int(x), int(y), i))
    else:
        ecows.append((int(x), int(y), i))
ncows.sort()
ecows.sort(key=lambda cow: cow[1])
stopping = [None]*n

for ncow in ncows:
    for ecow in ecows:
        if ncow[0] > ecow[0] and ecow[1] > ncow[1]:
            ntrav = ecow[1] - ncow[1]
            etrav = ncow[0] - ecow[0]

            if ntrav < etrav and stopping[ecow[2]] == None:
                stopping[ecow[2]] = ncow[0]
            if ntrav > etrav and stopping[ncow[2]] == None:
                stopping[ncow[2]] = ecow[1]
                break
eat = [-1]*n
for ncow in ncows:
    if stopping[ncow[2]] != None:
        eat[ncow[2]] = stopping[ncow[2]] - ncow[1]
for ecow in ecows:
    if stopping[ecow[2]] != None:
        eat[ecow[2]] = stopping[ecow[2]] - ecow[0]

for x in eat:
    if x == -1:
        print('Infinity')
    else:
        print(x)
