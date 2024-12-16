import math

# Объём Земли в км³
volume_earth = 1.08321 * 10**12

# Ввод радиуса теоретически возможной планеты
radius = float(input("Введите радиус случайной планеты: "))

# Вычисление объёма теоретической планеты
volume_planet = (4 / 3) * math.pi * (radius**3)

# Сравнение объёмов
if volume_planet > volume_earth:
    ratio = volume_planet / volume_earth
    print(f"Объём планеты Земля меньше в {ratio:.3f} раз")
else:
    ratio = volume_earth / volume_planet
    print(f"Объём планеты Земля больше в {ratio:.3f} раз")
