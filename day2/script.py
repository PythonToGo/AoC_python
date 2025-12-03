def is_invalid_id(n: int) -> bool:
    s = str(n)
    # not even number of digits
    if len(s) % 2 != 0:
        return False
    half = len(s) // 2
    return s[:half] == s[half:]


def parse_ranges(line: str):
    parts = line.strip().split(",")
    ranges = []
    for p in parts:
        if not p:
            continue
        a, b = p.split("-")
        ranges.append((int(a), int(b)))
    return ranges


def solve1(filename: str) -> int:
    with open(filename, "r", encoding="utf-8") as f:
        line = f.readline()
    ranges = parse_ranges(line)

    total = 0
    for start, end in ranges:
        for n in range(start, end + 1):
            if is_invalid_id(n):
                total += n
    return total

#############################################################
def is_invalid_id_p2(n: int) -> bool:
    s = str(n)
    length = len(s)
    
    # ignore one digit
    if length < 2:
        return False
    
    # ~ block length k:1 - length//2
    for k in range(1, length//2 + 1):
        if length % k != 0:
            continue
        
        block = s[:k]
        if block * (length // k) == s:
            return True
    return False

def solve2(filename: str) -> int:
    with open(filename, "r", encoding="utf-8") as f:
        line = f.readline()
    ranges = parse_ranges(line)
    
    total = 0
    for start, end in ranges:
        for n in range(start, end + 1):
            if is_invalid_id_p2(n):
                total += n
    return total


if __name__ == "__main__":
    print(solve1("input.txt"))
    print(solve2("input.txt"))

