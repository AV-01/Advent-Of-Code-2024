def calculate_area_and_perimeter(grid):
    def flood_fill(x, y, plant_type):
        stack = [(x, y)]
        visited.add((x, y))
        area = 0
        perimeter = 0

        while stack:
            cx, cy = stack.pop()
            area += 1

            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    if grid[nx][ny] == plant_type:
                        if (nx, ny) not in visited:
                            visited.add((nx, ny))
                            stack.append((nx, ny))
                    else:
                        perimeter += 1
                else:
                    perimeter += 1

        return area, perimeter

    rows, cols = len(grid), len(grid[0])
    visited = set()
    results = {}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for x in range(rows):
        for y in range(cols):
            if (x, y) not in visited:
                plant_type = grid[x][y]
                area, perimeter = flood_fill(x, y, plant_type)
                if plant_type not in results:
                    results[plant_type] = []
                results[plant_type].append({"area": area, "perimeter": perimeter})

    return results


with open('input.txt') as f:
    lines = f.read()
    lines = lines.split("\n")

plot = []
for line in lines:
    line_to_append = []
    for char in line:
        line_to_append.append(char)
    plot.append(line_to_append)

# plot = [
#     ["A", "A", "A", "A"],
#     ["B", "B", "C", "D"],
#     ["B", "B", "C", "C"],
#     ["E", "E", "E", "C"]
# ]

results = calculate_area_and_perimeter(plot)

ans = 0
# Output Results
for plant, regions in results.items():
    print(f"Plant Type: {plant}")
    for i, region in enumerate(regions):
        ans += region['area'] * region['perimeter']

print(ans)
