import random

def fitness(x, y):
    return x**2 + y**2

particles = [(random.uniform(-5,5), random.uniform(-5,5)) for _ in range(5)]
velocities = [(0,0) for _ in range(5)]

pbest = particles[:]
gbest = min(particles, key=lambda p: fitness(p[0], p[1]))

for _ in range(20):
    new_particles = []
    for i in range(len(particles)):
        x, y = particles[i]
        vx, vy = velocities[i]

        px, py = pbest[i]
        gx, gy = gbest

        vx = 0.5*vx + 0.5*(px - x) + 0.5*(gx - x)
        vy = 0.5*vy + 0.5*(py - y) + 0.5*(gy - y)

        x += vx
        y += vy

        new_particles.append((x, y))
        velocities[i] = (vx, vy)

        if fitness(x, y) < fitness(px, py):
            pbest[i] = (x, y)

    particles = new_particles
    gbest = min(pbest, key=lambda p: fitness(p[0], p[1]))

print("Best position:", gbest)