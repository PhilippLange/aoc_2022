import sys
sys.setrecursionlimit(100000)

file = './9/input.txt'
with open(file) as fn:
    raw = fn.read().splitlines()

v = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1),
}
c = [
        [
            v[i.split(" ")[0]],
            range(int(i.split(" ")[1]))
        ]
        for i in raw
    ][::-1]

def move_tail(t, hn):
    x = t[0]
    y = t[1]
    if abs(hn[0] - t[0]) > 1 or abs(hn[1] - t[1]) > 1:
        x = t[0]
        y = t[1]
        if hn[0] > t[0]:
            x += 1
        if hn[0] < t[0]:
            x -= 1
        if hn[1] > t[1]:
            y += 1
        if hn[1] < t[1]:
            y -= 1
    return (x, y)

def move(l, c, p, s):
    if not s:
        for i in range(l):
            s.append((0,0))
    if c:
        m = c.pop()
        for i in m[1]:
            s[0] = (s[0][0] + m[0][0], s[0][1] + m[0][1])
            for i in range(0, len(s)-1):
                s[i+1] = move_tail(s[i+1], s[i])
            p.add(s[-1])
        return move(l=l, c=c, p=p, s=s)
    else:
        return p

print(len(move(2, c.copy(), set(), list())))
print(len(move(10, c.copy(), set(), list())))