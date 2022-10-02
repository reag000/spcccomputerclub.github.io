class cow:
    def __init__(self, s, t, b):
        self.s, self.t, self.b = s, t, b

n = int(input())
s_cows = [cow(*map(int, input().split())) for _ in range(n)]
s_cows.sort(key=lambda x: x.s)
t_cows = sorted(s_cows, key=lambda x: x.t)
s_cows.append(cow(0, 0, 0))
i_s = i_t = 0
m = a = 0
for i in range(1, t_cows[n-1].t+1):
    if i == s_cows[i_s].s:
        d = abs(s_cows[i_s].b-a)
        a = max(0, a-s_cows[i_s].b)
        m += d if a == 0 else 0
        i_s += 1
        continue
    if i == s_cows[i_t].t:
        a += s_cows[i_t].b
        i_t += 1
        continue
print(m)
