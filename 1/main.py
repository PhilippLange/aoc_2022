file = './2/input.txt'
with open(file) as fn:
    raw = fn.read()

parsed = [ [ int(c) for c in e.split('\n') ] for e in raw.split('\n\n') ]
sum_elf = [ sum(c) for c in parsed ]
sum_elf.sort(reverse=True)
print(sum_elf[0])
print(sum(sum_elf[0:3]))