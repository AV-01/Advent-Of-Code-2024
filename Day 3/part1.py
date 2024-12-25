import re

# Path to the uploaded file
file_path = 'input.txt'

# Open and read the file
with open(file_path, 'r') as file:
    content = file.read()

# Define the regular expression pattern to match mul(X,Y) where X and Y are 1-3 digit numbers
pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

# Find all matches in the file
matches = re.findall(pattern, content)

# Process each match and calculate results
results = []
for match in matches:
    x, y = map(int, match)  # Convert captured groups to integers
    result = x * y
    results.append(result)

# Print the results
sum = 0
for res in results:
    sum += res

print(sum)
