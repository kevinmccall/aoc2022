fishes = []
inital_timers = None

fish_cycles = {
    0 : 0,
    1 : 0,
    2 : 0,
    3 : 0,
    4 : 0,
    5 : 0,
    6 : 0,
}
fish_queue = {}

class LanternFish:
    def __init__(self, internal_timer) -> None:
        self.internal_timer = internal_timer
    
    def reproduce(self, new_pool):
        self.internal_timer = 6
        new_pool.append(LanternFish(8))
    
    def step(self, new_pool):
        if self.internal_timer <= 0:
            self.reproduce(new_pool)
        else:
            self.internal_timer -= 1
    

with open('input', 'r') as reader:
    inital_timers = [int(x) for x in reader.readline().strip().split(",")]

# for time in inital_timers:
#     fish = LanternFish(time)
#     fishes.append(fish)
#     print(fish.internal_timer, end=',')

for time in inital_timers:
    fish_cycles[time] += 1

print("shmexy time")



# for day in range(256):
#     breeding_pond = []
#     # print(f"day {day}: ", end='')
#     for fish in fishes:
#         fish.step(breeding_pond)
#         # print(fish.internal_timer, end=',')
#     for newborn_fish in breeding_pond:
#         fishes.append(newborn_fish)
#         # print(newborn_fish.internal_timer, end=',')
#     # print()

days = 256

for day in range(days):
    print(f"day {day}:")
    reproducing_group = day % 7
    fish_queue[day + 2] = ((reproducing_group + 2) % 7, fish_cycles[reproducing_group])
    if day in fish_queue:
        group, amount = fish_queue[day]
        fish_cycles[group] += amount
        del fish_queue[day]
    for reproducing_group in fish_cycles:
        print(f"group {reproducing_group}: {fish_cycles[reproducing_group]}")
    
    if day == days - 1:
        for group, amount in fish_queue.values():
            fish_cycles[group] += amount

print(sum(fish_cycles.values()))
