if __name__ == "__main__":
    speed_ = input("Введите скорость (байт/сек.): ")    # Write your solution here
    time_ = input("Введите время загрузки (минут): ")
    price_ = input("Введите стоимость 2-го и послед. Гб (руб./Гб): ")
    size_ = int(speed_) * 60 * int(time_) / (1024 ** 3)
print(size_)  # Расчет размера
if int(size_) > 1:
    cost_ = (int(size_) - 1) * int(price_)
    print(cost_)
else: print("Цена: " + "0")
pass
