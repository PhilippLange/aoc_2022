import sys
sys.setrecursionlimit(100000)
file = './12/input.txt'
with open(file) as fn:
    raw = fn.read().splitlines()

D = [ list(i) for i in raw ]
L = [ [None]*len(i) for i in D ]

class P:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def height(self):
        char = D[self.x][self.y]
        if char == "S":
            char = "a"
        if char == "E":
            char = "z"
        return ord(char) - ord("a") + 1

    @property
    def finish(self):
            if D[self.x][self.y] == "E":
                return True
            return False

    @property
    def tuple(self):
        return (self.x, self.y)

    def __eq__(self, other):
        return isinstance(other, P) and self.tuple == other.tuple

    @property
    def length(self):
        return L[self.x][self.y]

    @length.setter
    def length(self, value):
        L[self.x][self.y] = value

    def update_length(self, l):
        if (self.length == None) or (l < self.length):
            self.length = l
            return True
        else:
            return False

    @property
    def neighbours(self):
        neighbors = []
        if self.x >= 1:
            neighbor = P(x=self.x-1, y=self.y)
            if neighbor.height - self.height <= 1:
                neighbors.append(neighbor)
        if self.x < len(D)-1:
            neighbor = P(x=self.x+1, y=self.y)
            if neighbor.height - self.height <= 1:
                neighbors.append(neighbor)
        if self.y >= 1:
            neighbor = P(x=self.x, y=self.y-1)
            if neighbor.height - self.height <= 1:
                neighbors.append(neighbor)
        if self.y < len(D[0])-1:
            neighbor = P(x=self.x, y=self.y+1)
            if neighbor.height - self.height <= 1:
                neighbors.append(neighbor)
        return neighbors

for x in range(len(D)):
    for y in range(len(D[0])):
        if D[x][y] == "S":
            S = P(x, y)
        if D[x][y] == "E":
            E = P(x, y)

def walk(a:P=S, l=0):
    if not a.update_length(l):
        return
    if a == E:
        return
    if E.length != None and a.length >= E.length:
        return
    for b in a.neighbours:
        walk(b, l+1)

walk()
print(E.length)