loaded_config = """# Rocket Ship Configuration File!
fuel_tanks=4
oxygen_tanks=3
initial_propulsion_level=84
$ End of file"""

parsed_config = {}
for line in loaded_config.split("\n"):
    try:
        key, value = line.split("=")
        parsed_config[key] = value
    except ValueError:
        print("Valor no valido")
        
print(parsed_config)