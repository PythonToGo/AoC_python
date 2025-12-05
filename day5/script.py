def solve1(filename: str) -> int:
    with open(filename, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f]
    
    # Find the blank line separator
    blank_line_idx = -1
    for i, line in enumerate(lines):
        if not line:
            blank_line_idx = i
            break
    
    # Parse ranges (before blank line)
    ranges = []
    for i in range(blank_line_idx):
        if lines[i]:
            start, end = map(int, lines[i].split('-'))
            ranges.append((start, end))
    
    # Parse available IDs (after blank line)
    available_ids = []
    for i in range(blank_line_idx + 1, len(lines)):
        if lines[i]:
            available_ids.append(int(lines[i]))
    
    # Count how many available IDs are fresh (fall into at least one range)
    fresh_count = 0
    for ingredient_id in available_ids:
        is_fresh = False
        for start, end in ranges:
            if start <= ingredient_id <= end:
                is_fresh = True
                break
        if is_fresh:
            fresh_count += 1
    
    return fresh_count


def solve2(filename: str) -> int:
    with open(filename, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f]
    
    # Find the blank line separator
    blank_line_idx = -1
    for i, line in enumerate(lines):
        if not line:
            blank_line_idx = i
            break
    
    # Parse ranges (before blank line)
    ranges = []
    for i in range(blank_line_idx):
        if lines[i]:
            start, end = map(int, lines[i].split('-'))
            ranges.append((start, end))
    
    # Sort ranges by start value
    ranges.sort()
    
    # Merge overlapping ranges
    merged = []
    for start, end in ranges:
        if not merged:
            merged.append((start, end))
        else:
            last_start, last_end = merged[-1]
            # If current range overlaps or is adjacent to the last merged range
            if start <= last_end + 1:
                # Merge: extend the last range if needed
                merged[-1] = (last_start, max(last_end, end))
            else:
                # No overlap: add as new range
                merged.append((start, end))
    
    # Calculate total number of IDs in all merged ranges
    total = 0
    for start, end in merged:
        total += (end - start + 1)
    
    return total


if __name__ == "__main__":
    filename = "input.txt"
    result = solve1(filename)
    print(result)
    
    result = solve2(filename)
    print(result)

