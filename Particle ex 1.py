import random

def fitness(x):
    return x**2

particles = [random.uniform(-10, 10) for _ in range(5)]
velocities = [0]*5

pbest = particles[:]
gbest = min(particles, key=fitness)

for _ in range(20):
    for i in range(len(particles)):
        velocities[i] = (0.5 * velocities[i] +
                         0.5 * (pbest[i] - particles[i]) +
                         0.5 * (gbest - particles[i]))

        particles[i] += velocities[i]

        if fitness(particles[i]) < fitness(pbest[i]):
            pbest[i] = particles[i]

    gbest = min(pbest, key=fitness)

print("Best solution:", gbest)