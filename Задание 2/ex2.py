import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Создаем матрицу заполненную случайными значениями
arr = np.array(np.random.randint(1,10,(5,5)))
print(arr)

# Решение СЛАУ
# 2x + 5y = 1
# x - 10y = 3
M1 = np.array([[2., 5.], [1., -10.]])  # Матрица (левая часть системы)
v1 = np.array([1., 3.])  # Вектор (правая часть системы)

print(np.linalg.solve(M1, v1))  # Ответом будет [1 -0.2]

# Построим тепловую карту на основе случайной матрицы
sns.heatmap(arr, annot=True, cmap='coolwarm')
plt.show()

# Построим гистограмму на основе случайной матрицы
# sns.histplot(arr, x = None)
sns.set(color_codes=True)
sns.set(style="white", palette="muted")
sns.histplot(arr)
plt.show()

# Построим график с шумом
noise = np.random.normal(0,0.5,100)
X = np.linspace(1, 100, 100)
Y = np.sin(X)

# print(X,Y,noise)

for i in range(len(X)):
    X[i] += noise[i]

plt.plot(X, Y)
plt.xlabel('ось x')
plt.ylabel('ось y')
plt.title('Заголовок')
plt.grid(True)
plt.show()