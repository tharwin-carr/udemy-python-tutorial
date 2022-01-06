def fahrenheit_to_celcius(f):
    celcius = (f - 32) * 5 / 9
    return celcius


print(fahrenheit_to_celcius(81))

def celcius_to_fahrenheit(c):
    fahrenheit = (c * 9) / 5 + 32
    return fahrenheit


print(celcius_to_fahrenheit(10))
