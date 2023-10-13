import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# Определение функции
def my_function(x):
    return np.sin(x)  # Пример функции, замените на свою функцию

# Создание данных
x = np.linspace(0, 2 * np.pi, 100)  # Диапазон значений x от 0 до 2*pi
y = my_function(x)  # Вычисление значений функции для всех x

# Создание фигуры и осей
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.12)  # Размещение кнопки

# Нарисовать график функции
line, = ax.plot(x, y, label='Функция')

# Определите точки для добавления на график
x_points = [np.pi/2, np.pi/2, np.pi/2, 3*np.pi/2, 3*np.pi/2]  # Пример значений x, в которых нужно отобразить точки
y_points = my_function(x_points)  # Значения функции в заданных точках

# Нарисуйте точки на графике с указанием описаний
scatter = ax.scatter(x_points, y_points, color='red', label='Точки')  # Красные точки

# Добавить метки к точкам
for i, txt in enumerate(y_points):
    ax.text(x_points[i], y_points[i], f'({x_points[i]:.2f}, {txt:.2f})', ha='right')

# Добавить заголовок и метки осей
plt.title('График функции с точками и метками')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')

# Функция для обработки нажатия кнопки
def toggle_points(event):
    if scatter.get_visible():
        scatter.set_visible(False)
    else:
        scatter.set_visible(True)
    plt.draw()

# Создание кнопки
ax_button = plt.axes([0.01, 0.01, .05, .05])  # Позиция кнопки
button = Button(ax_button, 'П 0')
button.on_clicked(toggle_points)  # Назначение функции на событие нажатия кнопки

# Показать график
plt.show()