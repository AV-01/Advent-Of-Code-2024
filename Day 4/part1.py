def count_horizontal(text):
    count = 0
    for i in range(len(text)-4):
        if text[i:i+4] == "XMAS" or text[i:i+4] == "SAMX":
            count +=1
    return count

def count_vertical(text_in_array):
    count = 0

    cols = len(text_in_array[0])

    rows = len(text_in_array)

    for x in range(cols):
        for y in range(rows - 3):
            try:
                vertical_string = (
                        text_in_array[y][x]
                        + text_in_array[y + 1][x]
                        + text_in_array[y + 2][x]
                        + text_in_array[y + 3][x]
                )
                # Check for matches
                if vertical_string in {"XMAS", "SAMX"}:
                    count += 1
            except IndexError:
                continue
    return count

def count_diagonal(text_in_array):
    c = 0
    rows = len(text_in_array)
    cols = len(text_in_array[0])
    for x in range(cols):
        for y in range(rows - 3):
            try:
                if y + 3 < rows and x + 3 < cols:
                    diagonal_string_lr = (
                            text_in_array[y][x]
                            + text_in_array[y + 1][x + 1]
                            + text_in_array[y + 2][x + 2]
                            + text_in_array[y + 3][x + 3]
                    )
                    if diagonal_string_lr in {"XMAS", "SAMX"}:
                        c += 1
                if y + 3 < rows and x - 3 >= 0:
                    diagonal_string_rl = (
                            text_in_array[y][x]
                            + text_in_array[y + 1][x - 1]
                            + text_in_array[y + 2][x - 2]
                            + text_in_array[y + 3][x - 3]
                    )
                    if diagonal_string_rl in {"XMAS", "SAMX"}:
                        c += 1
            except:
                continue
    return c

def find_xmas(text_in_array):
    c=0
    rows = len(text_in_array)
    cols = len(text_in_array[0])
    for x in range(cols):
        for y in range(rows):
            try:
                diagonal_string_lr1 = (
                        text_in_array[y-1][x-1]
                        + text_in_array[y][x]
                        + text_in_array[y+1][x + 1]
                )
                diagonal_string_rl2 = (
                        text_in_array[y+1][x-1]
                        + text_in_array[y][x]
                        + text_in_array[y-1][x + 1]
                )
                if diagonal_string_lr1 in {"MAS", "SAM"} and diagonal_string_rl2 in {"MAS", "SAM"}:
                    c += 1
                # if y + 3 < rows and x - 3 >= 0:
                #     diagonal_string_rl = (
                #             text_in_array[y][x]
                #             + text_in_array[y + 1][x - 1]
                #             + text_in_array[y + 2][x - 2]
                #             + text_in_array[y + 3][x - 3]
                #     )
                #     if diagonal_string_rl in {"XMAS", "SAMX"}:
                #         c += 1
            except:
                continue
    return c

with open("input.txt", 'r') as file:
    my_text = []
    for line in file:
        my_text.append(line)

    total_xmas = 0
    # for line in my_text:
    #     total_xmas += count_horizontal(line)
    # total_xmas += count_vertical(my_text)
    total_xmas += find_xmas(my_text)

    print(total_xmas)
