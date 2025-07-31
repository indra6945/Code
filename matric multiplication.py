p,q,r=map(int,input().split())
a= []
for i in range(p):
    t= list(map(int, input().split()))
    a.append(t)
b= []
for i in range(q):
    t= list(map(int, input().split()))
    b.append(t)
c = []
for i in range(p):
    t = []
    for j in range(r):
        t.append(0)
    c.append(t)
for i in range(p):
    for j in range(r):
        for k in range(q):
            c[i][j] = c[i][j] + a[i][k] * b[k][j]
for i in c:
    print(*i)
