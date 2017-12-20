#! /usr/bin/env python3


import re
import math
from collections import namedtuple


Particle = namedtuple('Particle', ['p', 'v', 'a'])
Vector = namedtuple('Vector', ['x', 'y', 'z'])


def slowest(particles):
    sorted_particles = sorted(particles, key=lambda x: magnitude(x.a))
    slowest = sorted_particles[0]
    return particles.index(slowest)


def simulate(particles):
    for i in range(50):
        particles = detect_collisions(particles)
        particles = [update(p) for p in particles]
        print(f'clock={i}, # of particles: {len(particles)}')


def detect_collisions(particles):
    positions = {}
    for i, p in enumerate(particles):
        if p.p in positions:
            positions[p.p].append(i)
        else:
            positions[p.p] = [i]

    collisions = []
    for pos, ps in positions.items():
        if len(ps) > 1:
            print(f'BOOM! {ps}')
            collisions.extend(ps)

    for idx in collisions[::-1]:
        del particles[idx]

    return particles


def manhattan_dist(v):
    x, y, z = v
    return abs(x) + abs(y) + abs(z)


def magnitude(v):
    x, y, z = v
    return math.sqrt(x**2 + y**2 + z**2)


def update(particle):
    p, v, a = particle
    vx = v.x + a.x
    vy = v.y + a.y
    vz = v.z + a.z
    px = p.x + vx
    py = p.y + vy
    pz = p.z + vz
    p = Particle(Vector(px, py, pz), Vector(vx, vy, vz), a)
    return p


def Input():
    with open('20_input.txt', 'r') as f:
        return [parse(count, line) for count, line in enumerate(f)]


def parse(i, line):
    seq = line.strip().split(', ')
    seqs = [re.findall(r'(-?\d+)', s) for s in seq]
    seqs = [Vector(*map(int, seq)) for seq in seqs]
    return Particle(p=seqs[0], v=seqs[1], a=seqs[2])


if __name__ == '__main__':
    particles = Input()
    print('part 1:', slowest(particles))
    simulate(particles)
