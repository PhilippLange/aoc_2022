file = './2/input.txt'
with open(file) as fn:
    raw = fn.read()

t = {
    "X": "r",
    "A": "r",
    "Y": "p",
    "B": "p",
    "Z": "s",
    "C": "s",
}

p = {
    "r": 1,
    "p": 2,
    "s": 3,
}

w = {
    ("r", "p"),
    ("p", "s"),
    ("s", "r"),
}

def score(a):
    r = p[a[1]]
    if a[0] == a[1]:
        return r + 3
    if (a[0], a[1]) in w:
        return r + 6
    return r

parsed = [ score([ t[i] for i in ln.split(" ") ]) for ln in raw.splitlines() ]
print(sum(parsed))