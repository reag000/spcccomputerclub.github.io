s = input()
t = input()
i = 0
while i < len(s):
    if s[i] == t[0]:
        k = i + 1
        c = 1
        l = i
        while k < len(s) and c < len(t) and s[k] == t[c]:
            if s[k] == s[i]:
                l = k
            k += 1
            c += 1
        if c == len(t):
            if k == len(s):
                s = s[:i]
                break
            else:
                s = s[:i] + s[k:]
                i = i - len(t)
                if i < 0: i = -1
        else:
            if k == len(s):
                break
            else:
                if l > i:
                    i = l - 1
                else:
                    i = k - 1
    i += 1
print(s)
