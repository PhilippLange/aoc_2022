file = './7/input.txt'
with open(file) as fn:
    raw = fn.read().splitlines()[::-1]

def build_tree(c, t={}):
    while c:
        e = c.pop()
        if e == "$ cd ..":
            break
        elif e == "$ ls":
            pass
        elif e[:4] == "$ cd":
            e = e[5:]
            if e not in t:
                t[e] = {}
            build_tree(c, t[e])
        else:
            e = e.split(" ")
            if e[0] == "dir":
                t[e[1]] = {}
            else:
                t[e[1]] = e[0]
    return t

def dir_size(t={},l={},wd=()):
    size = 0
    for k, v in t.items():
        if isinstance(v, dict):
            tmp = dir_size(v, l, wd)
            wd = wd + tuple(k)
            l[wd]=tmp
            size += tmp
        else:
            size += int(v)
    return size

t = build_tree(c=raw)
l = {}
s = dir_size(t, l)

print(sum([i for i in l.values() if i <= 100000]))

a = list(l.values())
a.sort()
print([ i for i in a if a[-1] - i <= 40000000 ][0])