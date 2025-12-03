def part1(filename: str) -> int:
    pos = 50
    count_zero = 0
    
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue # skip empty lines
            
            direction = line[0]
            distance = int(line[1:])
            
            if direction == "L":
                pos =(pos - distance) % 100
            elif direction == "R":
                pos = (pos + distance) % 100
            else:
                raise ValueError(f"Invalid direction: {direction}")
            
            if pos == 0:
                count_zero += 1
                
    return count_zero

def part2(filename: str) -> int: 
    pos = 50
    count_zero = 0
    
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue # skip empty lines
            
            direction = line[0]
            distance = int(line[1:])
            
            step = -1 if direction == 'L' else 1
            
            for _ in range(distance):
                pos = (pos + step) % 100
                if pos == 0:
                    count_zero += 1
                    
    return count_zero  

if __name__ == "__main__":
    filename = "input.txt"
    result = part1(filename)
    print(result)
    result = part2(filename)
    print(result)