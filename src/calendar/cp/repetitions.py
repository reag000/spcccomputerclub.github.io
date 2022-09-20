s = input()
m = c = 1
if len(s) == 1:
    print(1)
    quit()
else:
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            c += 1
        else:
            if c > m:
                m = c
            c = 1
m = c if c > m else m
print(m)
