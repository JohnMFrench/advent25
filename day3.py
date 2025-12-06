from util import get_input, get_args, copy_solution

args = get_args()
lines = get_input(day=3, is_practice=args.practice)

jolts: list[int] = []


def solve1() -> None:
    for bank in lines:
        l = max([c for c in bank][:-1])
        li = bank.index(l)
        r = max([c for c in bank][li + 1 :])
        num = int(l + r)

        print(f"max of {num} in {bank}")
        jolts.append(num)


def solve2() -> None:
    for bank in lines:
        snum = max([c for c in bank[:-11]])
        last_i = bank[:-11].index(snum)
        for k in range(10, -1, -1):
            if k == 0:
                rg = bank[last_i + 1:]
            else:
                rg = bank[last_i + 1 : -k]
            snum += max(rg)
            last_i += rg.index(snum[-1]) + 1
            print(f"looking at range of {rg} added an {snum[-1]}")

        print(f"max of {snum} in {bank}")
        jolts.append(int(snum))


solve2()


ans = sum(jolts)
print(ans)
copy_solution(ans)

