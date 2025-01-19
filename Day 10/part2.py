def parse_map(input_str):
    return [[int(char) for char in line] for line in input_str.splitlines()]

def find_trailheads(height_map):
    return [(r, c) for r, row in enumerate(height_map) for c, val in enumerate(row) if val == 0]

def count_trails(height_map, r, c, memo):
    rows, cols = len(height_map), len(height_map[0])

    # Memoization to avoid redundant calculations
    if (r, c) in memo:
        return memo[(r, c)]

    # If the current position is a '9', it is a valid endpoint for a trail
    if height_map[r][c] == 9:
        return 1

    trail_count = 0
    # Explore all valid neighbors
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and height_map[nr][nc] == height_map[r][c] + 1:
            trail_count += count_trails(height_map, nr, nc, memo)

    memo[(r, c)] = trail_count
    return trail_count

def calculate_ratings(height_map):
    trailheads = find_trailheads(height_map)
    total_rating = 0
    memo = {}

    for trailhead in trailheads:
        total_rating += count_trails(height_map, *trailhead, memo)

    return total_rating

# Example Input
with open('input.txt') as f:
    lines = f.read()
    lines = "\n".join(lines.split("\n"))

input_str = lines

# Parse and Calculate
height_map = parse_map(input_str)
total_rating = calculate_ratings(height_map)
print(f"Sum of ratings of all trailheads: {total_rating}")
