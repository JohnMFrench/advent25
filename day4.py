import os

from util import get_input, get_args, copy_solution

args = get_args()
grid = get_input(day=4, is_practice=args.practice)
grid = [list(line) for line in grid]


def get_num_adj(x: int, y: int, grid: list[list[str]]) -> int:
    adj = 0
    for ox in range(-1, 2):
        for oy in range(-1, 2):
            xi = x + ox
            yi = y + oy
            try:
                if (
                    xi < 0
                    or yi < 0
                    or xi >= len(grid[y])
                    or yi >= len(grid)
                    or (ox == 0 and oy == 0)
                ):
                    continue
                elif grid[yi][xi] == "@":
                    adj += 1
            except Exception as e:
                print(
                    f"IndexError with ({xi}, {yi}) in grid of width={len(grid[y])} and height={len(grid)}"
                )
    return adj


def solve1():
    ans = 0
    nmoved = float("inf")
    while nmoved > 0:
        movable_locs: list[tuple[int]] = []
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == "@":
                    adj = get_num_adj(x, y, grid)
                    # print(f"checking ({x},{y}) = {adj}")
                    if adj < 4:
                        movable_locs.append(tuple([x, y]))
                        ans += 1
        for ml in movable_locs:
            grid[ml[1]][ml[0]] = "x"
        nmoved = len(movable_locs)
        for y in range(len(grid)):
            print("".join(grid[y][:-5]))
        if nmoved == 0:
            break
        os.system("clear")
    print(ans)
    copy_solution(ans)


solve1()
