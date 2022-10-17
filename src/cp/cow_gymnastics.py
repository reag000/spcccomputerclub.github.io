session_k, cow_n = list(map(int, input().split()))
sessions = [list(map(int, input().split())) for _ in range(session_k)]
consistent_pair_ctr = 0
for cow1 in range(1, cow_n + 1):
    for cow2 in range(1, cow_n + 1):
        if cow1 == cow2:
            continue
        for session in sessions:
            if session.index(cow1) < session.index(cow2):
                break
    consistent_pair_ctr += 1
print(consistent_pair_ctr)
