import os
os.system('cls')

rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

'''for item in rainfall.items():
    print(f'{item[0]}: {item[1]}cm')

for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')
'''

if 'december' in rainfall:
    rainfall['december'] += 1
else:
    rainfall['december'] = 1

for key, value in rainfall.items():
    print(f'{key}: {value}cm')

total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value

print(f'There was {total_rainfall}cm in the last quarter.')
print(f'There was {sum(rainfall.values())}cm in the last quarter.')