def check_steady_increase(new_list):
    rate_of_changes = []
    for i in range(len(new_list)-1):
        rate_of_changes.append(abs(new_list[i]-new_list[i+1]))
        if not (new_list[i] < new_list[i+1]):
            return False
    only_rates = set(rate_of_changes)
    for x in only_rates:
        if x > 3 or x < 1:
            return False
    return True

def check_steady_decrease(new_list):
    rate_of_changes = []
    for i in range(len(new_list)-1):
        rate_of_changes.append(abs(new_list[i]-new_list[i+1]))
        if not (new_list[i] > new_list[i+1]):
            return False
    only_rates = set(rate_of_changes)
    for x in only_rates:
        if x > 3 or x < 1:
            return False
    return True

def check_prob_dampner(new_list):
    # print(new_list)
    for i in range(len(new_list)):
        test_list = new_list[:i] + new_list[i+1:]
        if check_steady_increase(test_list) or check_steady_decrease(test_list):
            return True
    return False

total_safe = 0
with open("input.txt", "r") as file:
    for line in file:
        # Split each line into two parts
        parts = line.split()
        parts = list(map(int, parts))
        # Append to respective lists
        if check_steady_increase(parts) or check_steady_decrease(parts):
            total_safe += 1
        elif check_prob_dampner(parts):
            total_safe += 1

print(total_safe)