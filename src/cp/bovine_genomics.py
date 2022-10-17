n, m = list(map(int, input().split()))
spotty_cows = [list() for _ in range(m)] # columns
for _ in range(n):
    genomes = input()
    for i in range(m):
        spotty_cows[i].append(genomes[i])
plain_cows = [list() for _ in range(m)]
for _ in range(n):
    genomes = input()
    for i in range(m):
        plain_cows[i].append(genomes[i])
mutation_ctr = 0
for i in range(m):
    if len(set(spotty_cows[i]).intersection(set(plain_cows[i]))) == 0:
        mutation_ctr += 1
print(mutation_ctr)
