file = './8/input.txt'
with open(file) as fn:
    raw = fn.read()

parsed = [ i for i in raw.splitlines() ]

vt = set()
vs = []

def is_visible(p, vt=vt, d=parsed):
    xb1 = range(0, p[0]+1)
    xb2 = range(p[0], len(d))
    yb1 = range(0, p[1]+1)
    yb2 = range(p[1], len(d[0]))
    if len([ True for x in xb1 if d[x][p[1]] < d[p[0]][p[1]] ]) == len(xb1)-1:
        vt.add(p)
        return True
    if len([ True for x in xb2 if d[x][p[1]] < d[p[0]][p[1]] ]) == len(xb2)-1:
        vt.add(p)
        return True
    if len([ True for y in yb1 if d[p[0]][y] < d[p[0]][p[1]] ]) == len(yb1)-1:
        vt.add(p)
        return True
    if len([ True for y in yb2 if d[p[0]][y] < d[p[0]][p[1]] ]) == len(yb2)-1:
        vt.add(p)
        return True

def score_view(p, vs=vs, d=parsed):
    s = [1, 1, 1, 1]
    x = p[0]
    y = p[1]
    while (x-s[0] > 0) and (d[x][y] > d[x-s[0]][y]):
        s[0] += 1
    while (x+s[1] < len(d)-1) and (d[x][y] > d[x+s[1]][y]):
        s[1] += 1
    while (y-s[2] > 0) and (d[x][y] > d[x][y-s[2]]):
        s[2] += 1
    while (y+s[3] < len(d[0])-1) and (d[x][y] > d[x][y+s[3]]):
        s[3] += 1
    vs.append(s[0]*s[1]*s[2]*s[3])

for x in range(len(parsed)):
    for y in range(len(parsed[0])):
        is_visible((x, y))
        score_view((x, y))

print(len(vt))
vs.sort()
print(vs[-1])