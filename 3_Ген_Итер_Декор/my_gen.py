
def solar_system_func(*args):
    data = list(args)
    while data:
        next = data.pop(0)
        new_value = (yield next)
        if new_value:
            data.append(new_value)


planets = ['Mercury', 'Venus', 'Earth']

solar_system = solar_system_func
for planet in planets:
    print(f'I am - {solar_system_func(planet)}')
    if planet == 'Venus':
        planet = solar_system_func.send('Mars')
        print(f'I am - {planet}')

