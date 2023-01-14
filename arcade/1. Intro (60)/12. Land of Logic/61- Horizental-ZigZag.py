def p(o):
    for i in o:
        print(i)

n = 4
ans = [[0 for j in range(n)] for i in range(n)]
f = [[0 for _ in range(n)] for _ in range(n)]
p(f[0])

o = []
c = 1

for i, v in enumerate(ans):
    l = []
    if i%2 == 0:
        print('odd')
        for j in range(len(v)):
            l.append(j)
            f[i][j] = c
            c = c + 1
    else:
        for j in range(len(v) -1, -1, -1):
            l.append(j)
            f[i][j] = c
            c = c + 1
        print('even')
    o.append(l)

p(o)
p(f)

