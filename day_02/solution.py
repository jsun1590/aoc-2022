def part_1():
    score = 0
    rules = [[3, 0, 6], [6, 3, 0], [0, 6, 3]]
    with open("input.txt") as fh:
        for line in fh.readlines():
            them = ord(line.strip().split()[0]) - ord("A")
            us = ord(line.strip().split()[1]) - ord("X")
            score += us + 1
            res = rules[us][them]
            score += res
    return score
            
def part_2():
    score = 0
    rules = [[3, 1, 2], [1, 2, 3], [2, 3, 1]]
    with open("input.txt") as fh:
        for line in fh.readlines():
            them = ord(line.strip().split()[0]) - ord("A")
            res = ord(line.strip().split()[1]) - ord("X")        
            us = rules[res][them]
            score  += res * 3
            score += us
            
    return score

print(part_1())
print(part_2())
