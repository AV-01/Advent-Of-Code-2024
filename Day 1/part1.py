left = []
right = []

# Read the file
with open("input.txt", "r") as file:
    for line in file:
        # Split each line into two parts
        parts = line.split()
        # Append to respective lists
        if len(parts) == 2:
            left.append(int(parts[0]))
            right.append(int(parts[1]))
left.sort()
right.sort()

total_dist = 0
for i in range(len(left)):
    total_dist += abs( left[i] - right[i])

print(total_dist)