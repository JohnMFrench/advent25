import os

from tqdm import tqdm

from util import get_input, get_args, copy_solution

args = get_args()
lines = get_input(day=7, is_practice=args.practice)

# store beams in a list bc there can be multiple beams occupying the same space
beams: list[int] = []

# for pt 2, map the location of a beam and the number of instances at that location index
bmap: dict[int, int] = {}
SC = "^"  # split char
nsplits = 0

# find starting beam
beams.append(lines[0].index("S"))
bmap[beams[0]] = 1

# iterate through all the lines containing splitters
for i in range(len(lines[1:])):
    line = lines[i]
    lsplits: list[int] = []  # splits this line
    i = 0
    while SC in line[i:]:
        if SC in line[i:]:
            lsplits.append(line[i:].index(SC) + i)
            i = lsplits[-1] + 1

    # calculate the beams for the next y-index
    nbeams: list[int] = []
    nbmap: dict[int, int] = {}
    for b in bmap.keys():
        if b in lsplits:
            if b > 0:
                if b - 1 in bmap.keys():
                    bmap[b - 1] += bmap[b]
                else:
                    nbmap[b - 1] = bmap[b]
            if b < len(line) - 1:
                if b + 1 in bmap.keys():
                    bmap[b + 1] += bmap[b]
                else:
                    nbmap[b + 1] = bmap[b]
            nsplits += 1
            bmap[b] = 0
        else:
            nbeams.append(b)

    # append new beams as keys (can't modify dict during loop
    for bi, n in nbmap.items():
        bmap[bi] = n
    beams = list(nbeams)

    # print the new row
    for pi in range(len(line)):
        if line[pi] == SC:
            print(SC, end="")
        elif pi in beams:
            print("|", end="")
        else:
            print(".", end="")
    print("")

# pt 1
# print(nsplits)
# copy_solution(nsplits)

# pt 2
ans = sum(bmap.values())
print(ans)
copy_solution(ans)
