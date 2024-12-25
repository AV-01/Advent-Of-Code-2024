with open('input.txt') as f:
    lines = f.read()
    lines = lines.split("\n")[0]

# turn into bunch of letters

mem = []
print(lines)

id = 0
num_free_space = 0
for i in range(len(lines)):
    if i%2 == 1:
        mem_to_append = []
        if int(lines[i]) == 0: continue
        for i in range(int(lines[i])):
            mem_to_append.append(".")
            num_free_space+=1
        mem.append(mem_to_append)
    else:
        mem_to_append = []
        if int(lines[i]) == 0: continue
        for i in range(int(lines[i])):
            mem_to_append.append(str(id))
        mem.append(mem_to_append)
        id += 1

def fix_filesystem(this_mem):
    front_index = 0
    back_index = len(this_mem)-1
    while front_index < back_index:
        if this_mem[front_index][0] == ".":
            while this_mem[back_index][0] == ".":
                back_index -= 1
            if len(this_mem[back_index]) > len(this_mem[front_index]):
                back_index -= 1
                continue
            while len(this_mem[back_index]) < len(this_mem[front_index]):
                this_mem[back_index].append(".")
            temp = this_mem[front_index]
            this_mem[front_index] = this_mem[back_index]
            this_mem[back_index] = temp
        front_index += 1
    return this_mem

def remerge(array):
    result = []
    dot_buffer = []
    for sublist in array:
        # Separate dots and non-dots
        dots = [x for x in sublist if x == '.']
        non_dots = [x for x in sublist if x != '.']

        # Handle non-dots
        if non_dots:
            # Flush the dot buffer before adding non-dot sublist
            if dot_buffer:
                result.append(dot_buffer)
                dot_buffer = []
            result.append(non_dots)

        # Handle dots
        if dots:
            dot_buffer.extend(dots)

    # Flush any remaining dots at the end
    if dot_buffer:
        result.append(dot_buffer)
    return result

for i in range(10000):
    mem = fix_filesystem(mem)
    mem = remerge(mem)

# for i in mem:
#     print("".join(i), end='')
# print("".join(mem))
# print(fix_filesystem(mem))

print(mem)

relative_index = 0
checksum = 0
for i in mem:
    for x in i:
        if x == ".":
            relative_index+=1
            continue
        checksum += relative_index * int(x)
        relative_index += 1

print(checksum)
