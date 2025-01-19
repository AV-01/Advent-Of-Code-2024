import re
import math

machines = []

with open("input.txt","r") as f:
    index = 0
    machine_dict = {}
    for line in f:
        if index == 0:
            a = [int(s) for s in re.findall(r'\d+', line)]
            machine_dict["A"] = a
            index += 1
        elif index == 1:
            a = [int(s) for s in re.findall(r'\d+', line)]
            machine_dict["B"] = a
            index += 1
        elif index == 2:
            a = [int(s) for s in re.findall(r'\d+', line)]
            machine_dict["Target"] = [a[0] + 10000000000000, a[1] + 10000000000000]
            machines.append(machine_dict)
            machine_dict = {}
            index +=1
        else:
            index = 0

def calculate_end_position(buttonA, buttonB, pressA, pressB):
    return (buttonA[0]*pressA + buttonB[0]*pressB, buttonA[1]*pressA + buttonB[1]*pressB)


def find_optimal_pos(buttonA, buttonB, target):
    D = buttonA[0]*buttonB[1] - buttonA[1]*buttonB[0]
    D_x = target[0]*buttonB[1] - target[1]*buttonB[0]
    D_y = buttonA[0]*target[1] - buttonA[1]*target[0]
    A = D_x/D
    B = D_y/D
    if int(A) == A and int(B) == B:
        return (A, B)
    return (0,0)
    # numerator = target[1] - (buttonB[1]*(target[0]/buttonB[0]))
    # denominator = buttonA[1] - ((buttonA[0]*buttonB[1])/buttonB[0])
    # print(numerator/denominator)
    # a = int(numerator/denominator)
    # # print(a)
    # b= (target[0]-(buttonA[0]*a))/buttonB[0]
    # print(b)
    # if int(a) == a and int(b) == b and a > 0 and b >0:
    #     return (a, b)
    # return (0,0)


t = 0
for machine in machines:
    tokens = find_optimal_pos(machine['A'], machine['B'], machine['Target'])
    t += tokens[0]*3
    t += tokens[1]*1

print(t)
# print(find_optimal_pos([17,86],[84,37],[7870,6450]))