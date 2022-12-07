file = './6/input.txt'
with open(file) as fn:
    raw = fn.read()

def find_marker(s, l):
    i = 0
    while True:
        if len(set(s[i:i+l])) == l:
            return i+l
        i += 1

print(find_marker(raw, 4))
print(find_marker(raw, 4) + find_marker(raw[find_marker(raw, 4):], 14))