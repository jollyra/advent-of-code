#! /usr/bin/env python3
''' start: 5:35 '''


import re
from collections import namedtuple
from util import manhattan_distance_3d
from pprint import pprint


Particle = namedtuple('Particle', ['p', 'v', 'a'])
Vector = namedtuple('Vector', ['x', 'y', 'z'])


def main(particles):
    for i in range(1000000000):
        particles = detect_collisions(particles)
        particles = [update(p) for p in particles]
        pprint(f'{i} # of particles {len(particles)}')


def detect_collisions(particles):
    positions = {}
    for i, p in enumerate(particles):
        if p.p in positions:
            positions[p.p].append(i)
        else:
            positions[p.p] = [i]

    # pprint(positions)
    for pos, ps in positions.items():
        if len(ps) > 1:
            print(f'collision {ps}')
            for p in ps[::-1]:
                del particles[p]

    return particles


def accel_vector(particle):
    return manhattan_distance_3d((0, 0, 0), particle.a)


def manhattan_dist(particle):
    return manhattan_distance_3d((0, 0, 0), particle.p)


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
    print('')
    particles = Input()
    main(particles)
