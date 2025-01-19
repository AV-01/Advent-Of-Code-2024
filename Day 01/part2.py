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

def count_num_in_right(num):
    total_count = 0
    for i in right:
        if i == num:
            total_count+=1
    return total_count

similitary_score = 0

for x in left:
    similitary_score += count_num_in_right(x) * x

print(similitary_score)