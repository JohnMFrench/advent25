from util import get_input, get_args

args = get_args()
lines = get_input(day=2, is_practice=args.practice)


def is_valid_id(sid: str) -> bool:
    if "0" in (start[0], end[0]):
        return False
    n = len(sid) // 2
    return sid[:n] != sid[n:]


def part_1():
    rgs = [l.split("-") for l in lines[0].split(",")]
    invalid_ids: list[int] = []

    for start, end in rgs:
        has_leading_zero = start[0] == "0" or end[0] == "0"
        for sn in range(int(start), int(end) + 1):
            if not is_valid_id(str(sn)) or has_leading_zero:
                invalid_ids.append(int(sn))

    print(sum(invalid_ids))


def is_valid_id2(sid: str) -> bool:
    for i in range(len(sid)):
        for i2 in range(i+1, len(sid)):
            # print(f'checking {sid[i:i2]}')
            if sid.count(sid[i:i2]) >= 2 and sid[i:i2] != '' and sid.replace(sid[i:i2], '') == '':
                # print(f'found {sid} to be invalid with repeating segment of {sid[i:i2]}')
                return False
    return True


def part_2():
    rgs = [l.split("-") for l in lines[0].split(",")]
    invalid_ids: list[int] = []

    for start, end in rgs:
        has_leading_zero = start[0] == "0" or end[0] == "0"
        if has_leading_zero:
            pass
            # print(f'{start} or {end} has leading zero ({start[0]}, {end[0]}')
        for sn in range(int(start), int(end) + 1):
            if not is_valid_id2(str(sn)) or has_leading_zero:
                invalid_ids.append(int(sn))

    # print(invalid_ids)
    print(sum(invalid_ids))

part_2()

