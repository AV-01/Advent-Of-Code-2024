import os

dir = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.join(dir, "input.txt")

with open(file_name) as f:
    txt = f.read()
    lines = txt.split("\n")


print(lines)
orderings = [[int(val) for val in line.split("|")] for line in lines[:lines.index("")]]
instructions = [[int(val) for val in line.split(",")] for line in lines[lines.index("")+1:]]


def works(inst: list):
    for order in orderings:
        try:
            i1, i2 = inst.index(order[0]), inst.index(order[1])
            if i1 > i2:
                return (i1, i2)
        except:
            pass

    return (0, 0)

t = 0

for inst in instructions:

    if works(inst) == (0, 0):
        continue

    while True:
        i1, i2 = works(inst)

        if (i1, i2) == (0, 0):
            break

        inst[i1], inst[i2] = inst[i2], inst[i1]

    t += inst[len(inst)//2]

print(t)