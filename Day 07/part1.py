import itertools

with open("input.txt") as f:
    equations = [line.strip() for line in f if line.strip()]

print(equations)

cal = []
for eq in equations:
    final_ans, nums = eq.split(":")
    final_ans = int(final_ans)
    my_nums = list(map(int, nums.split()))
    cal.append([final_ans, my_nums])

def generate_combinations(length):
    return list(itertools.product([0, 1, 2], repeat=length))

def test_combo(current_cal):
    target = current_cal[0]
    numbers = current_cal[1]
    all_combos = generate_combinations(len(numbers))

    for combo in all_combos:
        result = numbers[0]
        for i in range(1, len(numbers)):
            if combo[i] == 0:
                result += numbers[i]
            elif combo[i] == 1:
                result *= numbers[i]
            elif combo[i] == 2:
                result = int(str(result) + str(numbers[i]))
        if result == target:
            return True
    return False

current_sum = 0
for entry in cal:
    if test_combo(entry):
        current_sum += entry[0]
        print(entry)

print(current_sum)
