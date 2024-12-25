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
        for i in range(int(lines[i])):
            mem.append(".")
            num_free_space+=1
    else:
        for i in range(int(lines[i])):
            mem.append(str(id))
        id += 1

# print(mem)

front_index = 0
back_index = len(mem)-1
# print(len(mem)-num_free_space)
my_str = "0099811188827773336446555566.............."
while front_index < back_index:
    if mem[front_index] == ".":
        while mem[back_index] == ".":
            back_index -= 1
        mem[front_index] = mem[back_index]
        mem[back_index] = "."
    front_index += 1


checksum = 0
for i in range(len(mem)):
    if mem[i] == ".":
        break
    checksum += i * int(mem[i])

print(checksum)
