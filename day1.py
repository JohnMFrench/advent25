from util import get_input, get_args

args = get_args()
lines = get_input(day=1, is_practice=args.practice)

dial = 50  # dial starts at position 50
dial_rg = 100  # dial has 100 positions (0 - 99)
nhits = 0  # num of times dial is pointing to 0

# each line contains a dial turn
for turn in lines:
    drct = turn[0]  # direction is first character in each instruction
    nt = int(turn[1:]) % dial_rg  # num positions turned, normalized to 0-99

    # check if this turn will be a complete cycle
    ncycles = int(turn[1:]) // dial_rg # the number of complete cycles in a turn
    nhits += ncycles # add number of complete cycles to the number of zeroes

    # check if the dial started on zero, e.g. landed on it
    if dial == 0:
        nhits += 1
    # check if the dial will pass zero during the turn
    elif (drct == 'L' and dial - nt < 0) or (drct == 'R' and dial + nt > 100):
        nhits += 1

    # normalize the dial position into 0-99 range
    if drct == 'L':
        dial -= nt
        if dial < 0:
            dial += dial_rg
    else:
        dial += nt
        if dial > 99:
            dial = dial % dial_rg


print(f"Dial is in position {dial}")
print(f"Hit zero position {nhits} times")

