even_sum = 0

while True:
    number = int(input("Введите число (0 для выхода): "))
    if number == 0:
        break
    if number % 2 == 0:
        even_sum += number

print(even_sum)

