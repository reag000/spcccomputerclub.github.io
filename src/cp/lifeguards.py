n = int(input())
lifeguards = [list(map(int, input().split())) for _ in range(n)]
max_time = 1000
max_time_covered = 0
for i in range(n):
    time_covered = 0
    for t in range(1, max_time + 1):
        for j in range(n):
            if j != i:
                if t >= lifeguards[j][0] and t < lifeguards[j][1]:
                    time_covered += 1
                    break
    max_time_covered = max(time_covered, max_time_covered)
print(max_time_covered)