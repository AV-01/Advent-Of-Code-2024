def calculate_area_and_sides(grid):
    def flood_fill(x, y, plant_type):
        stack = [(x, y)]
        visited.add((x, y))
        area = 0
        sides = 0
        boundary = set()

        while stack:
            cx, cy = stack.pop()
            area += 1

            for i, (dx, dy) in enumerate(directions):
                nx, ny = cx + dx, cy + dy

                if 0 <= nx < rows and 0 <= ny < cols:
                    if grid[nx][ny] == plant_type:
                        if (nx, ny) not in visited:
                            visited.add((nx, ny))
                            stack.append((nx, ny))
                    else:
                        boundary.add((cx, cy))
                else:
                    boundary.add((cx, cy))

        # Calculate sides by counting turns in the boundary
        boundary_list = list(boundary)
        boundary_list.sort()  # Ensure consistent traversal

        for i in range(len(boundary_list)):
            current = boundary_list[i]
            next_point = boundary_list[(i + 1) % len(boundary_list)]

            if current[0] != next_point[0] and current[1] != next_point[1]:
                sides += 1

        return area, sides

    rows, cols = len(grid), len(grid[0])
    visited = set()
    results = {}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for x in range(rows):
        for y in range(cols):
            if (x, y) not in visited:
                plant_type = grid[x][y]
                area, sides = flood_fill(x, y, plant_type)
                if plant_type not in results:
                    results[plant_type] = []
                results[plant_type].append({"area": area, "sides": sides})

    return results

# Example Input
plot = [
    ["A", "A", "A", "A"],
    ["B", "B", "C", "D"],
    ["B", "B", "C", "C"],
    ["E", "E", "E", "C"]
]

# Example Input
plot = [
    ["A", "A", "A", "A"],
    ["B", "B", "C", "D"],
    ["B", "B", "C", "C"],
    ["E", "E", "E", "C"]
]

# Calculate
results = calculate_area_and_sides(plot)

# Output Results
for plant, regions in results.items():
    print(f"Plant Type: {plant}")
    for i, region in enumerate(regions):
        print(f"  Region {i + 1}: Area = {region['area']}, Sides = {region['sides']}")
