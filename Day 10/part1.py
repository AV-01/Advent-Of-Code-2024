def parse_map(input_str):
    return [[int(char) for char in line] for line in input_str.splitlines()]

def find_trailheads(height_map):
    return [(r, c) for r, row in enumerate(height_map) for c, val in enumerate(row) if val == 0]

def dfs(height_map, start, visited):
    rows, cols = len(height_map), len(height_map[0])
    stack = [start]
    reachable_nines = set()

    while stack:
        r, c = stack.pop()
        if (r, c) in visited:
            continue
        visited.add((r, c))

        # If it's a 9, add to reachable set
        if height_map[r][c] == 9:
            reachable_nines.add((r, c))
            continue

        # Explore neighbors
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) not in visited and height_map[nr][nc] == height_map[r][c] + 1:
                    stack.append((nr, nc))

    return reachable_nines

def calculate_scores(height_map):
    trailheads = find_trailheads(height_map)
    total_score = 0

    for trailhead in trailheads:
        visited = set()
        reachable_nines = dfs(height_map, trailhead, visited)
        total_score += len(reachable_nines)

    return total_score


with open('input.txt') as f:
    lines = f.read()
    lines = "\n".join(lines.split("\n"))

print(lines)
# Example Input
input_str = lines

# Parse and Calculate
height_map = parse_map(input_str)
total_score = calculate_scores(height_map)
print(f"Sum of scores of all trailheads: {total_score}")
