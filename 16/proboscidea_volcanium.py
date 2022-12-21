data = None
p1 = 0
p2 = 0
with open("testinput.txt", "r", encoding="utf8") as reader:
    data = [x.strip() for x in reader.readlines()]

flow_rates = {}
pipes = set()
# AA : (0, ["DD", "II", "BB"])

for line in data:
    split = line.split(" ")
    valve = split[1]
    leading_valves = [x.strip(",") for x in split[9:]]
    flow_rate = int(split[4][5:-1])
    flow_rates[valve] = (flow_rate, leading_valves)


def calculate_flow_rate(current_valve, time_left, current_pressure, opened_pipes):
    if time_left <= 0:
        return 0

    pipe_data = flow_rates[current_valve]
    open_pressure = 0
    if current_valve not in opened_pipes:
        open_pressure = pipe_data[0]
        opened_pipes.add(current_valve)

    time_left -= 1
    return max(
        calculate_flow_rate(x, time_left - 1, current_pressure, opened_pipes)
        for x in pipe_data[1]
    )
