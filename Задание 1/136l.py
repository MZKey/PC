import mod

n = int(input("Введите n = "))
a = [0] * n
a = mod.init_array(a)

res = mod.calc136l(a)

print("\nRes = ", res)
