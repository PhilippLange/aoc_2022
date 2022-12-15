file = './3/input.txt'
with open(file) as fn:
    raw = fn.read()

def score(s):
    if s.islower():
        return ord(s) - 96
    else:
        return ord(s) - 38

parsed = raw.splitlines()
d1 = [ [ bp[:len(bp)//2], bp[len(bp)//2:] ] for bp in parsed ]
d1 = [ set({ j for j in i[0] if j in i[1] }) for i in d1 ]
d1 = [ sum([ score(j) for j in i ]) for i in d1 ]
print(sum(d1))

d2 = [ (
        set(parsed[j])
        .intersection(set(parsed[j+1]))
        .intersection(set(parsed[j+2]))
    ) for j in [i*3 for i in range(len(parsed)//3) ] ]
print(sum([ sum([ score(j) for j in i ]) for i in d2 ]))