file = './4/input.txt'
with open(file) as fn:
    raw = fn.read()

parsed = [ [ [ int(j) for j in i.split("-") ] for i in l.split(",") ] for l in raw.splitlines() ]

def pair_contains(p1, p2):
    return (
        (p1[0] <= p2[0] and p1[1] >= p2[1]) or
        (p2[0] <= p1[0] and p2[1] >= p1[1])
    )

def pair_overlaps(p1, p2):
    return (
        p2[0] <= p1[0] <= p2[1] or
        p2[0] <= p1[1] <= p2[1] or
        p1[0] <= p2[0] <= p1[1] or
        p1[0] <= p2[1] <= p1[1]
    )

d1 = [ a for a in parsed if pair_contains(a[0], a[1]) ]
print(len(d1))
d2 = [ a for a in parsed if pair_overlaps(a[0], a[1]) ]
print(len(d2))