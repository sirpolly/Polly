def count_positive_even_numbers(numbers):
    count = 0
    for number in numbers:
        if number > 0 and number % 2 == 0:
            count += 1
    return count


# Ввод десяти чисел
numbers = []
print("Введите 10 чисел:")
for _ in range(10):
    num = int(input())  # Считываем число
    numbers.append(num)  # Добавляем число в список

# Подсчитываем положительные четные числа
result = count_positive_even_numbers(numbers)

print(f"Количество положительных четных чисел: {result}")
