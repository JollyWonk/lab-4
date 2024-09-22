def sum_of_digits(number):

    if len(str(abs(number))) != 4:
        raise ValueError("Число повинно бути чотиризначним!")

    return sum(int(digit) for digit in str(abs(number)))

try:
    number = int(input("Введіть чотиризначне число: "))
    result = sum_of_digits(number)
    print(f"Сума цифр числа: {result}")
except ValueError as e:
    print(f"Помилка: {e}")
