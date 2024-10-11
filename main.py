import os
os.system('cls')

new_planet = ''
planets = []

while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
        print(planets)
    new_planet = input('Enter a new planet or done if done: ')
#end while

for planeta in planets:
    print(planeta)