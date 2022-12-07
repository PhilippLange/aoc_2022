import copy

file = './5/input.txt'
with open(file) as fn:
    raw = fn.read()

s = raw.split("\n\n")[0].splitlines()
idx = [ int(i)-1 for i in s[-1].split("   ") ]
s = [ [ j[(i*4)+1] for j in s[:-1] if j[(i*4)+1] != " " ][::-1] for i in idx ]

p = [
        [
            int(m.split(' ')[1]),
            int(m.split(' ')[3])-1,
            int(m.split(' ')[5])-1
        ]
    for m in raw.split("\n\n")[1].splitlines()
]


d1 = copy.deepcopy(s)
for m in p:
    for i in range(m[0]):
        d1[m[2]].append(d1[m[1]].pop())

print(''.join([ i[-1] for i in d1 ]))

d2 = copy.deepcopy(s)
for m in p:
    d2[m[2]] = d2[m[2]] + d2[m[1]][-1 * m[0]:]
    d2[m[1]] = d2[m[1]][:-1 * m[0]]

print(''.join([ i[-1] for i in d2 ]))