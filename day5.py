import os

from tqdm import tqdm

from util import get_input, get_args, copy_solution

args = get_args()
lines = get_input(day=5, is_practice=args.practice)

# first lines are ranges then ids delimited by blank line
rngns: list[tuple[int]] = []
ids: list[int] = []

for line in tqdm(lines):
    if line == "":
        continue
    elif "-" in line:
        rng = tuple([int(sn) for sn in line.split("-")])
        rngns.append(rng)
    else:
        ids.append(int(line))
ninitrngns = len(rngns)

# # pt 1
# ans: int = 0
# for iid in ids:
#     solved = False
#     for rng in rngns:
#         if solved == False:
#             if iid >= rng[0] and iid <= rng[1]:
#                 ans += 1
#                 solved = True
#                 break

# # print(ans)
# copy_solution(ans)

# ans = sum([rg[1]+1 - rg[0] for rg in rngns])
# # print(ans)
# copy_solution(ans)

# print(rngns)
# pt 2
while True:
    rngns = sorted(rngns, key=lambda rg: (rg[0], rg[1]))
    chg = False
    print("sorted")
    print(rngns)
    for i in range(len(rngns) - 1):
        if not chg:
            # compare each range with the next
            if rngns[i + 1][0] <= rngns[i][1]:
                print(f"merging {rngns[i]} and {rngns[i+1]}", end="")
                rngns[i] = tuple(
                    [
                        min([rngns[i][0], rngns[i + 1][0]]),
                        max([rngns[i][1], rngns[i + 1][1]]),
                    ]
                )
                rngns.pop(i + 1)
                print(f" into {rngns[i]}")
                chg = True
                break
    if not chg:
        break

print(rngns)
print(len(rngns))
ans = sum([rg[1] + 1 - rg[0] for rg in rngns])
print(ans)
copy_solution(ans)
