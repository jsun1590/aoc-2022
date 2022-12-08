with open("input.txt") as fh:
    line = fh.read().rstrip()

def part_1():
    queue = []
    for i in range(len(line)-4):
        queue.append(line[i])
        if i >= 4:
            if len(queue) == len(set(queue)):
                return i
                break
            queue.pop(0)
            
def part_2():
    queue = []
    for i in range(len(line)-4):
        queue.append(line[i])
        if i >= 14:
            if len(queue) == len(set(queue)):
                return i
                break
            queue.pop(0)

print(part_1())
print(part_2())