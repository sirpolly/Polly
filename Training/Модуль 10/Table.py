def print_table():
    rows_count = 6
    cols_count = 6
    for i in range(rows_count):
        row = []
        for j in range(cols_count):
            value = i + j * 2
            row.append(value)
        # Увеличенное расстояние между столбцами
        print("  ".join(f"{num:2}" for num in row))


# Вызов функции для печати таблицы
print_table()
