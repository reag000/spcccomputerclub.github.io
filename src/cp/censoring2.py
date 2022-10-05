s = input()
t = input()
n = ''
for c in s:
    n += c
    if n.endswith(t):
        n = n[:-len(t)]
print(n)
