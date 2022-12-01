from collections import defaultdict
cals = defaultdict(int)
elf = 0

with open("input.txt") as f:
    for line in f.readlines():
        if line == "\n":
            elf += 1
        else:
            cals[elf] += int(line.strip())
        
        
# part 1
print(max(cals.values()))
# part 2
print(sum(sorted(cals.values())[-3:]))