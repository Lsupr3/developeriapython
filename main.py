import os
os.system('cls')

amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
ordenada = sorted(regular_satellite_moons, reverse=True)

print(ordenada)

