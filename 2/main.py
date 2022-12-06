file = './2/input.txt'
with open(file) as fn:
    raw = fn.read()

t = {
    "A": "r",
    "X": "r",
    "B": "p",
    "Y": "p",
    "C": "s",
    "Z": "s",
}

p = {
    "r": 1,
    "p": 2,
    "s": 3,
}

w = {
    "r": "p",
    "p": "s",
    "s": "r",
}

l = {v: k for k, v in w.items()}

def score(a):
    r = p[a[1]]
    if a[0] == a[1]:
        return r + 3
    if w[a[0]] ==  a[1]:
        return r + 6
    return r

def transform(a):
    a[0] = t[a[0]]
    if a[1] == 'Y':
        a[1] = a[0]
    if a[1] == 'Z':
        a[1] = w[a[0]]
    if a[1] == 'X':
        a[1] = l[a[0]]
    return a

parsed = [ score([ t[i] for i in ln.split(" ") ]) for ln in raw.splitlines() ]
print(sum(parsed))
parsed = [ score(transform(ln.split(" "))) for ln in raw.splitlines() ]
print(sum(parsed))