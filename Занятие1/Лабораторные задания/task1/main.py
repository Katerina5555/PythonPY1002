if __name__ == "__main__":
    DAYS_OF_YEAR = 365  # количество дней в году

    start_year = input("Введите год рождения: ")  # TODO запросить у пользователя год рождения
    current_year = input("Введите текущий год: ")  # TODO запросить у пользователя текущий год
    Total_days = (int(current_year) - int(start_year)) * DAYS_OF_YEAR
    print(Total_days)# TODO посчитать и распечатать количество прожитых дней
