import os
os.system('cls')

planet = {
    'name': 'Earth',
    'moons': 1
}

#print(planet['pepe'])
planet['moons'] = 79
print(planet.get('moons'))
planet['diametro'] = {
    'polar': 133709,
    'equatorial': 142984    
}

print(planet.keys())
print(planet.values())
print(f'{planet["name"]} polar diameter: {planet["diametro"]["equatorial"]}, {planet["diametro"]["polar"]}')
print(planet)