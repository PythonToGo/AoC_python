def max_joltage_for_bank(line: str) -> int:
    digits =[int(c) for c in line.strip()]
    n = len(digits)
    
    # less than 2 digits
    if n < 2:
        return 0
    
    # suffix_max[i] = i or more digits suffix max
    suffix_max = [0] * n
    suffix_max[-1] = digits[-1]
    for i in range(n-2, -1, -1):
        suffix_max[i] = max(digits[i], suffix_max[i+1])
    
    best = -1
    
    for i in range(n-1):
        cand = 10 * digits[i] + suffix_max[i+1]
        if cand > best:
            best = cand
    
    return best

def solve1(filename: str) -> int:
    total = 0
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue # skip empty lines
            total += max_joltage_for_bank(line)
    return total

#############################################################
def max_joltage_for_bank_p2(line: str, k: int= 12) -> int:
    s = line.strip()
    digits = [c for c in s]
    n = len(digits)
    
    if n <= k:
        return int(s)
    
    drops = n - k
    stack = []
    
    for d in digits:
        while stack and drops > 0 and stack[-1] < d:
            stack.pop()
            drops -= 1
        stack.append(d)
        
    result_digits = stack[:k]
    return int("".join(result_digits))

def solve2(filename: str) -> int:
    total = 0
    
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue # skip empty lines
            total += max_joltage_for_bank_p2(line)
    return total    

#############################################################

if __name__ == "__main__":
    print(solve1("input.txt"))
    print(solve2("input.txt"))