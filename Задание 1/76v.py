print("Введите натуральные числа от 1 до 8")
k = int(input("k = "))
l = int(input("l = "))
m = int(input("m = "))
n = int(input("n = "))

while not 1 <= k <= 8 or not 1 <= l <= 8 or not 1 <= m <= 8 or not 1 <= n <= 8:
    print("\nВведите натуральные числа от 1 до 8")
    k = int(input("k = "))
    l = int(input("l = "))
    m = int(input("m = "))
    n = int(input("n = "))

if (k - m)**2 + (l - n)**2 == 5:
    print(f"\nКонь на поле ({k},{l}) \033[31mугрожает\033[0m полю ({m},{n})")
else:
    print(f"\nКонь на поле ({k},{l}) \033[31mне угрожает\033[0m полю ({m},{n})")