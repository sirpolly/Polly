def count_grades(grades):
    excellent = 0  # Количество пятерок
    good = 0  # Количество четверок
    average = 0  # Количество троек

    for grade in grades:
        if grade == 5:
            excellent += 1
        elif grade == 4:
            good += 1
        elif grade == 3:
            average += 1

    return excellent, good, average


# Ввод количества студентов
n = int(input("Введите количество студентов в классе: "))

# Ввод оценок
grades = []
print("Введите оценки (3, 4 или 5) для каждого студента:")
for i in range(n):
    grade = int(input(f"Оценка студента {i + 1}: "))
    while grade not in [3, 4, 5]:
        print("Ошибка: введите только 3, 4 или 5.")
        grade = int(input(f"Оценка студента {i + 1}: "))
    grades.append(grade)

# Подсчет оценок
excellent, good, average = count_grades(grades)

# Определение, кого больше
if excellent > good and excellent > average:
    print("Сегодня больше отличников.")
elif good > excellent and good > average:
    print("Сегодня больше хорошистов.")
elif average > excellent and average > good:
    print("Сегодня больше троечников.")
else:
    print(
        "Количество отличников, хорошистов и троечников одинаково или ошибки в данных."
    )
