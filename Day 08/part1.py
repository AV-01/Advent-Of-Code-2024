import os
import string

dir = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.join(dir, "input.txt")



with open(file_name) as f:
    txt = f.read()
    lines = txt.split("\n")
    h, w = len(lines), len(lines[0])

frequencies = string.ascii_letters + string.digits

freq_dict = {freq : [] for freq in frequencies}

def in_range(x,y):
    return 0 <= x < h and 0 <= y < w

for y in range(h):
    for x in range(w):
        char = lines[y][x]
        if char != ".":
            freq_dict[char].append((y, x))

all_pos = set()

def replace_char_at_index(string, index, new_char):
    return string[:index] + new_char + string[index + 1:]

for char in freq_dict:
    for y1, x1 in freq_dict[char]:
        for y2, x2 in freq_dict[char]:
            if (y1, x1) == (y2, x2):
                continue

            dy, dx = y1 - y2, x1 - x2
            locs = [(x1 + dx, y1 + dy), (x2 - dx, y2 - dy)]



            all_pos.update(loc for loc in locs if in_range(loc[0], loc[1]))

# for line in lines:
#     print(line)
print(len(all_pos))
# print(freq_dict)
