with open("input.txt") as fh:
    lines = [line.strip() for line in fh.readlines()]

def part_1():
    total = 0
    for line in lines:
        s1 = set()
        s2 = set()
        for i, c in enumerate(line):
            if i < len(line) // 2:
                s1.add(c)
            else:
                s2.add(c)
        same = s2.intersection(s1)
        p = ord("".join(same)) + 1
        total += p - ord("a") if p > ord("a") else p - ord("A") + 26
    return total

def part_2():
    total = 0
    for i in range(0, len(lines), 3):
        s = [set(), set(), set()]
        for j in range(3):
            s[j] = {c for c in lines[i+j]}
        
        same = s[0].intersection(s[1]).intersection(s[2])
        p = ord("".join(same)) + 1
        total += p - ord("a") if p > ord("a") else p - ord("A") + 26
    return total

print(part_1())

print(part_2())
