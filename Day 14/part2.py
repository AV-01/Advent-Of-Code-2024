import re
import time

w,h = 101, 103

robots = []
with open("input.txt", "r") as f:
    for line in f:
        p_v = line.split(" ")
        robot_dict = {}
        robot_dict['p'] = [int(s) for s in re.findall(r'\d+', p_v[0])]
        robot_dict['v'] = [int(s) for s in p_v[1].replace("v=","").split(",")]
        robots.append(robot_dict)

def get_new_pos(p, v, times = 1):
    new_x = p[0] + v[0]*times
    new_y = p[1] + v[1]*times
    while new_x >= w:
        new_x -= w
    while new_x < 0:
        new_x += w
    while new_y >= h:
        new_y -= h
    while new_y < 0:
        new_y += h


    return (new_x, new_y)

repeat_amt = 293
for i in range(len(robots)):
    for a in range(repeat_amt):
        robots[i]['p'] = get_new_pos(robots[i]['p'], robots[i]['v'])

def display():
    indexes = []
    for a in range(0,h):
        for b in range(0,w):
            on_square = 0
            for x in range(len(robots)):
                if robots[x]['p'][0] == b and robots[x]['p'][1] ==a:
                    on_square += 1
                    indexes.append(x)
            if on_square == 0:
                print(".", end="")
            else:
                print(on_square, end="")
        print()

while True:
    print(f"Current time {repeat_amt}: ")
    display()
    for i in range(len(robots)):
        for a in range(1):
            robots[i]['p'] = get_new_pos(robots[i]['p'], robots[i]['v'])
    repeat_amt += 1
    time.sleep(0.2)