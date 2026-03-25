import random
import string

target = "HELLO"

def fitness(s):
    return sum(1 for i in range(len(s)) if s[i] == target[i])

def random_string():
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(len(target)))

population = [random_string() for _ in range(6)]

for generation in range(100):
    population = sorted(population, key=fitness, reverse=True)

    if population[0] == target:
        break

    parents = population[:2]

    # Crossover
    child = parents[0][:3] + parents[1][3:]

    # Mutation
    child = list(child)
    if random.random() < 0.3:
        idx = random.randint(0, len(child)-1)
        child[idx] = random.choice(string.ascii_uppercase)

    population[-1] = ''.join(child)

print("Best match:", population[0])