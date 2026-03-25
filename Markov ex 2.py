import random

states = ["A", "B"]

def step(state, action):
    if state == "A":
        return ("B", 10) if action == "right" else ("A", 0)
    else:
        return ("A", 5) if action == "left" else ("B", 0)

policy = {"A": "right", "B": "left"}

state = "A"
total_reward = 0

for _ in range(10):
    action = policy[state]
    state, reward = step(state, action)
    total_reward += reward

print("Total reward:", total_reward)