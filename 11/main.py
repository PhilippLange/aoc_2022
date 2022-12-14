file = './11/input.txt'
with open(file) as fn:
    raw = fn.read().splitlines()

M = []

class Monkey:
    def __init__(self, i = "  Starting items: 79, 98", o = "  Operation: new = old * 19", d = "  Test: divisible by 23",  a = ["    If true: throw to monkey 2","    If false: throw to monkey 3"]):
        self.c = 0
        self.i = [int(j) for j in i[18:].split(",")]
        self.d = int(d.split(" ")[-1])
        self.a = {
            True: int(a[0].split(" ")[-1]),
            False: int(a[1].split(" ")[-1])
        }
        self.o = o[19:].replace("old", "{0}")

    def add(self, i):
        self.i.append(i)
    
    def inspect(self, v):
        self.c += 1
        return int(eval(self.o.format(v))) // 3

    def check(self, v):
        if v % self.d:
            return self.a[False]
        return self.a[True]

    def operation(self):
        while self.i:
            item = self.inspect(self.i.pop())
            M[self.check(item)].add(item)

    def __lt__(self, other):
        return self.c < other.c

for i in range(len(raw)):
    if raw[i].split(" ")[0] == "Monkey":
        M.append(Monkey(
            i=raw[i+1],
            o=raw[i+2],
            d=raw[i+3],
            a=[raw[i+4], raw[i+5]],
        ))

for i in range(20):
    for m in M:
        m.operation()
M = sorted(M)
print(M[-2].c * M[-1].c)
