from collections import deque 

q1 = 0
q2 = 0
data = []
with open('input', 'r') as reader:
    for line in reader:
        data.append(line.strip())

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
incomplete_lines = []

# Too high
for line in data:
    stack = deque()
    line_over = False
    for char in line:
        if line_over:
            continue
        if char in "([{<":
            stack.append(char)
        else:
            top = stack.pop()
            val = scores[char]
            if top == "(" and not char == ")":
                q1 += val
                print(f"Expected ), but found {char} instead")
                line_over = True
            if top == "[" and not char == "]":
                print(f"Expected ], but found {char} instead")
                q1 += val
                line_over = True
                
            if top == "{" and not char == "}":
                print(f"Expected }}, but found {char} instead")
                q1 += val
                line_over = True
                
            if top == "<" and not char == ">":
                print(f"Expected >, but found {char} instead")
                q1 += val
                line_over = True
    incomplete_lines.append(stack)
                
scores = []

for stack in incomplete_lines:
    current_score = 0
    while len(stack) > 0:
        starting_bracket = stack.pop()
        current_score *= 5

        if starting_bracket == "(":
            current_score += 1
        elif starting_bracket == "[":
            current_score += 2
        elif starting_bracket == "{":
            current_score += 3
        elif starting_bracket == "<":
            current_score += 4
    scores.append(current_score)

scores.sort()

print(q1)
print(scores[int(len(scores) / 2) + 1])





