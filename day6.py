import os

from tqdm import tqdm

from util import get_input, get_args, copy_solution

args = get_args()
lines = get_input(day=6, is_practice=args.practice)

ops: list[str] = [op for op in lines[-1].split(" ") if op]
oprs = []
op = ''
res: list[int] = []

def solve1():
    for i in range(len(lines))[:-1]:
        nums = [n for n in lines[i].split(" ") if n]
        for j in range(len(nums)):
            if i == 0:
                oprs.append([])
            oprs[j].append(int(nums[j]))

    for i in range(len(oprs)):
        if ops[i] == '+':
            res.append(sum(oprs[i]))
        elif ops[i] == '*':
            val = 1
            for opr in oprs[i]:
                val *= opr
            res.append(val)
        elif ops[i] == '-':
            val = oprs[i][0]
            for opr in oprs[i][1:]:
                val -= opr
            res.append(val)
        else:
            val = oprs[i][0]
            for opr in oprs[i][1:]:
                val /= opr
            res.append(val)

def solve2():
    oprs: list[int] = []
    cols = []
    for x in range(len(lines[0])):
        cols.append('')
        for y in range(len(lines)):
            cols[x] += lines[y][x]
    for i in range(len(cols)):
        for ops in ('+', '-', '*', '/'):
            if ops in cols[i]:
                # print(f"replacing {ops} in {cols[i]}")
                cols[i] = cols[i].replace(ops, "")
                cols[i] = cols[i].strip()
                op = ops
                break
        cols[i] = cols[i].strip()
        if cols[i].isdigit():
            oprs.append(int(cols[i]))
        elif cols[i].strip() == '':
            print(f"compiling {op} ({oprs})")
            oprs = oprs[::-1]
            if op == '+':
                res.append(sum(oprs))
            elif op == '*':
                val = 1
                for opr in oprs:
                    val *= opr
                res.append(val)
            elif op == '-':
                val = oprs[0]
                for opr in oprs[1:]:
                    val -= opr
                res.append(val)
            elif op == '/':
                val = oprs[0]
                for opr in oprs[1:]:
                    val /= opr
                res.append(val)
            op = ''
            oprs = []
    # print(cols)
    print(f"compiling {op} ({oprs})")
    oprs = oprs[::-1]
    if op == '+':
        res.append(sum(oprs))
    elif op == '*':
        val = 1
        for opr in oprs:
            val *= opr
        res.append(val)
    elif op == '-':
        val = oprs[0]
        for opr in oprs[1:]:
            val -= opr
        res.append(val)
    elif op == '/':
        val = oprs[0]
        for opr in oprs[1:]:
            val /= opr
        res.append(val)


solve2()


print(res)

ans = sum(res)

print(ans)
copy_solution(ans)
