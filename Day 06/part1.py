direction = "up"

def find_player():
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "^":
                return (x, y)

def is_in_bounds(position):
    return 0 <= position[0] < len(map[0]) and 0 <= position[1] < len(map)

def find_next_position():
    if direction == "up":
        return (player_loc[0], player_loc[1] - 1)
    if direction == "down":
        return (player_loc[0], player_loc[1] + 1)
    if direction == "left":
        return (player_loc[0] - 1, player_loc[1])
    if direction == "right":
        return (player_loc[0] + 1, player_loc[1])

def turn_right(current_direction):
    directions = ["up", "right", "down", "left"]
    index = directions.index(current_direction)
    return directions[(index + 1) % 4]

# Read input file
with open("input.txt") as f:
    txt = f.read()
    map = [line for line in txt.split("\n") if line.strip()]

player_loc = find_player()
visited = set()

while is_in_bounds(player_loc):
    visited.add(player_loc)
    next_possible_pos = find_next_position()

    if is_in_bounds(next_possible_pos) and map[next_possible_pos[1]][next_possible_pos[0]] == "#":
        direction = turn_right(direction)
    elif is_in_bounds(next_possible_pos):
        player_loc = next_possible_pos
    else:
        break

for line in map:
    print(line)

print(len(visited))
