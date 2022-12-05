with open("input.txt") as fh:
    lines = [line.strip() for line in fh.readlines()]
    
def part_1():
    total = 0
    for line in lines:
        l = line.split(",")[0]
        r = line.split(",")[1]
        
        min1 = int(l.split("-")[0])
        max1 = int(l.split("-")[1])
        min2 = int(r.split("-")[0])
        max2 = int(r.split("-")[1])
        
        if (min1 <= min2 and max2 <= max1) or (min2 <= min1 and max1 <= max2):
            total += 1
    return total

def part_2():
    total = 0
    for line in lines:
        l = line.split(",")[0]
        r = line.split(",")[1]
        min1 = int(l.split("-")[0])
        max1 = int(l.split("-")[1])
        min2 = int(r.split("-")[0])
        max2 = int(r.split("-")[1])
        
        s1 = set(range(min1, max1 + 1))
        s2 = set(range(min2, max2 + 1))
        
        if len(s1.intersection(s2)):
            total += 1
    return total

print(part_1())
print(part_2())