states = ["A", "B"]
actions = ["left", "right"]

rewards = {
    ("A", "right"): 10,
    ("A", "left"): 0,
    ("B", "left"): 5,
    ("B", "right"): 0
}

gamma = 0.9
V = {"A": 0, "B": 0}

for _ in range(10):
    new_V = {}
    for s in states:
        values = []
        for a in actions:
            values.append(rewards.get((s,a), 0) + gamma * V[s])
        new_V[s] = max(values)
    V = new_V

print("State values:", V)