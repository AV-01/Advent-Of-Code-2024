array = [['0', '0'], ['9', '9', '.'], ['1', '1', '1'], ['7', '7', '7'], ['2'], ['4', '4', '.'],
         ['3', '3', '3'], ['.'], ['.', '.', '.'], ['.'], ['5', '5', '5', '5'], ['.'],
         ['6', '6', '6', '6'], ['.'], ['.', '.', '.'], ['.'], ['8', '8', '8', '8'], ['.', '.', '.']]

result = []
dot_buffer = []  # Temporary storage for dots to merge them when necessary

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

print(remerge(array))
