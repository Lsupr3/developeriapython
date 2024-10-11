import os
import numpy as np
# pip import numpy

os.system('cls')
planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

print(planet_moons.keys())
print(len(planet_moons))
print(np.mean(list(planet_moons.values())))