results = [
    number for number in range(10, 100) if number == (number // 10) * (number % 10) * 3
]

if results:
    print("Найдены двузначные числа:", ", ".join(map(str, results)))
else:
    print("Нет двузначных чисел, равных утроенному произведению своих цифр.")
