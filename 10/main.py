file = './10/input.txt'
with open(file) as fn:
    raw = fn.read().splitlines()

c = {
    "noop": 1,
    "addx": 2,
}

d = [ 
    (
        i.split(" ")[0],
        int(i.split(" ")[1]) if len(i.split(" ")) == 2 else 0
    )
    for i in raw
]

ln = []
lc = []
cc = 0
cs = 0
for i in d:
    for j in [20, 60, 100, 140, 180, 220]:
        if cc < j <= cc + c[i[0]]:
            lc.append((cs+1)*j)

    for j in range(1, c[i[0]] + 1):
        if len(ln) == 40:
            print("".join(ln))
            ln = []
        if cs <= len(ln) <= cs + 2:
            ln.append("#")
        else:
            ln.append(".")

    cc += c[i[0]]
    cs += i[1]
print("".join(ln))
print(sum(lc))