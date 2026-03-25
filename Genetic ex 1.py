import random

# Fitness function: maximize f(x) = x^2
def fitness(x):
    return x**2

# Create initial population
population = [random.randint(-10, 10) for _ in range(6)]

for generation in range(10):
    # Selection (top 2)
    population = sorted(population, key=fitness, reverse=True)
    parents = population[:2]

    # Crossover
    child = (parents[0] + parents[1]) // 2

    # Mutation
    if random.random() < 0.3:
        child += random.randint(-2, 2)

    population[-1] = child

print("Best solution:", max(population, key=fitness))