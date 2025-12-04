def solve1(filename: str) -> int:
    with open(filename, 'r', encoding='utf-8') as f:
        grid = [line.rstrip("\n") for line in f if line.strip()]
        
    H = len(grid)
    W = len(grid[0])
    
    # 8 adj (dr, dc)
    direction = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
    ]
    
    acc = 0
    
    for r in range(H):
        for c in range(W):
            if grid[r][c] != '@':
                continue
            
            neighbors = 0
            
            for dr, dc in direction:
                nr, nc = r + dr, c + dc
                if 0 <= nr < H and 0 <= nc < W:
                    if grid[nr][nc] == '@':
                        neighbors += 1
            
            if neighbors < 4:
                acc += 1
    
    return acc


#############################################################
def read_grid(filename: str):
    with open(filename, 'r', encoding='utf-8') as f:
        grid = [line.rstrip("\n") for line in f if line.strip()]
    return grid

def count_neighbors(grid, r, c):
    H = len(grid)
    W = len(grid[0])
    
    direction = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
    ]
    
    count = 0
    for dr, dc in direction:
        nr, nc = r + dr, c + dc
        if 0 <= nr < H and 0 <= nc < W:
            if grid[nr][nc] == '@':
                count += 1
    return count


def solve2(filename: str) -> int:
    grid = read_grid(filename)
    # Convert strings to lists for mutability
    grid = [list(row) for row in grid]
    H = len(grid)
    W = len(grid[0])
    
    removed_total = 0
    
    while True:
        to_remove = []
        
        for r in range(H):
            for c in range(W):
                if grid[r][c] != '@':
                    continue
                neighbors = count_neighbors(grid, r, c)
                if neighbors < 4:
                    to_remove.append((r, c))
            
        if not to_remove:
            break
    
        for r, c in to_remove:
            grid[r][c] = '.'
        
        removed_total += len(to_remove)
    return removed_total

if __name__ == "__main__":
    filename = "input.txt"
    result = solve1(filename)
    print(result)
    
    result = solve2(filename)
    print(result)