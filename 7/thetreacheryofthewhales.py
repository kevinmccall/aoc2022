data = []
with open('input', 'r') as reader:
    data = [int(x) for x in reader.readline().strip().split(',')]

costs = []
evaluating_range = range(-len(data), len(data))
for x in evaluating_range:
    sus = 0
    for pos in data:
        cost_to_move = abs(pos - x)

        sus += sum(range(cost_to_move + 1))
    costs.append(sus)

print(min(costs))
