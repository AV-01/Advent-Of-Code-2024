import re

# Path to the uploaded file
file_path = 'input.txt'

# Open and read the file
with open(file_path, 'r') as file:
    content = file.read()

# Define patterns
mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'  # Matches mul(X,Y)
instruction_pattern = r'do\(\)|don\'t\(\)'  # Matches do() or don't()

# Initialize state
enabled = True  # mul instructions are enabled by default

# Track results
results = []

# Split content into instructions and process sequentially
tokens = re.split(r'(do\(\)|don\'t\(\))', content)  # Split at do() or don't()

for token in tokens:
    token = token.strip()  # Remove extra spaces/newlines
    if token == "do()":
        enabled = True  # Enable future mul() instructions
    elif token == "don't()":
        enabled = False  # Disable future mul() instructions
    else:
        if enabled:  # Process mul() only when enabled
            matches = re.findall(mul_pattern, token)
            for match in matches:
                x, y = map(int, match)  # Convert captured numbers to integers
                result = x * y
                results.append(result)

# Output results
sum = 0
if results:
    for res in results:
        sum += res
else:
    print("No valid mul() instructions executed.")

print(sum)