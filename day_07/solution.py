from pprint import pprint
from collections import defaultdict
fs = {}
cache = defaultdict(int)
curr = fs
folders = []

with open("input.txt") as fh:
    lines = [line.rstrip() for line in fh.readlines()]

for line in lines:
    arg0 = line.split()[-2]
    arg1 = line.split()[-1]
    if line.startswith("$ cd"):
        if arg1 == "..":
            curr = curr[".."]
            folders.pop()
            continue
        try:
            folders.append(folders[-1]+arg1)
        except:
            folders.append("/")
        curr[arg1] = {}
        curr[arg1][".."] = curr
        curr = curr[arg1]
    elif line.startswith("$ ls"):
        continue
    else:
        if arg0 != "dir":
            for k in folders:
                cache[k] += int(arg0)

total = 0
for i in cache:
    if cache[i]< 100000:
        total += cache[i]

target = cache["/"] - 40000000
valid = filter(lambda x : x>=target, cache.values())


# part 1
print(total)

# part 2
print(min(valid))