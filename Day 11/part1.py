

with open('input.txt') as f:
    lines = f.read()
    lines = lines.split(" ")

print(lines)

def blink(stones):
    new_stones = []
    for i in stones:
        if i == "0":
            new_stones.append("1")
        elif len(i) % 2 == 0:
            new_stones.append(str(int(i[0:int(len(i)/2)])))
            new_stones.append(str(int(i[int(len(i)/2):])))
        else:
            new_stones.append(str(int(i)*2024))
    return new_stones

for i in range(25):
    lines = blink(lines)

print(len(lines))