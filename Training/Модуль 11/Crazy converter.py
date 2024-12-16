# Константы для конвертации
EUR_TO_USD = 1.05  # 1 евро = 1.05 доллара
USD_TO_RUB = 103.01  # 1 доллар = 103.01 рубля

# Запрашиваем у пользователя стоимость покупки в евро
cost_in_euro = float(input("Стоимость покупки в евро: "))

# Конвертируем евро в доллары
cost_in_usd = cost_in_euro * EUR_TO_USD

# Конвертируем доллары в рубли
cost_in_rub = cost_in_usd * USD_TO_RUB

# Округляем результат до двух знаков после запятой
cost_in_rub_rounded = round(cost_in_rub, 2)

# Выводим результат
print(f"Стоимость в рублях: {cost_in_rub_rounded:.2f}")
