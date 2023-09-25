import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]  # Пример значений x
y = [0, 1, 4, 9, 16, 25]  # Пример значений y (например, квадратичная функция)

plt.plot(x, y)

plt.xlabel('Значения X')
plt.ylabel('Значения Y')
plt.title('График функции Y = X^2')

plt.show()