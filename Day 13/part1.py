import re
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
            machine_dict["Target"] = a
            machines.append(machine_dict)
            machine_dict = {}
            index +=1
        else:
            index = 0

def calculate_end_position(buttonA, buttonB, pressA, pressB):
    return (buttonA[0]*pressA + buttonB[0]*pressB, buttonA[1]*pressA + buttonB[1]*pressB)


def find_optimal_pos(buttonA, buttonB, target):
    current_sol = (0,0)
    current_cost = 4000
    for a in range(101):
        for b in range(101):
            curr_sol = calculate_end_position(buttonA, buttonB, a, b)
            if curr_sol[0] == target[0] and curr_sol[1] == target[1]:
                if a*3 + b < current_cost:
                    current_sol = (a,b)
                    current_cost = a*3 + b
    return current_sol

t = 0
for machine in machines:
    tokens = find_optimal_pos(machine['A'], machine['B'], machine['Target'])
    t += tokens[0]*3
    t += tokens[1]*1

print(t)