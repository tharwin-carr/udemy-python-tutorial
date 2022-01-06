vehicle = {
    'model': 'Veloster',
    'make': 'Hyundai',
    'year': 2019,
    'mileage': '15400'
}

for x, y in vehicle.items():
    print(x, y)

vehicle2 = vehicle.copy()

vehicle2['number of tires'] = 4

print(f'vehicle = {vehicle}')
print(f'vehicle2 = {vehicle2}')