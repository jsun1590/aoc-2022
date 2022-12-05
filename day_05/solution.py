
import copy


with open("input.txt") as fh:
    lines = [line.rstrip("\n") for line in fh.readlines()]
    
line_len = len(lines[0])
num_containers = (line_len+1)//4
build = True
containers = [[] for _ in range(num_containers)]
ins = []

for line in lines:
    if line == "":
        build = False
        continue
    if build:
        for i in range(1, line_len+1, 4):
            if line[i] != " " and not line[i].isdigit():
                containers[(i+1)//4].append(line[i])
    else:
        tmp = []
        for i in range(3):
            tmp.append(int(line.split()[1+i*2]))
        ins.append(tmp)

def part_1():
    c = copy.deepcopy(containers)
    top_row = ""
    for i in ins:
        for _ in range(i[0]):
            c[i[2]-1].insert(0, c[i[1]-1].pop(0))

    for i in range(num_containers):
        top_row += c[i][0]
    return top_row

def part_2():
    c = copy.deepcopy(containers)
    top_row = ""
    for i in ins:
        for j in range(i[0]):
            c[i[2]-1].insert(0, c[i[1]-1].pop(i[0]-j-1))

    for i in range(num_containers):
        top_row += c[i][0]
    return top_row

print(part_1())
print(part_2())