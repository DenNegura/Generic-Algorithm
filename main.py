from generic_algorithm import generic_algorithm
from visual import view
from settings import Settings

settings = Settings()

g_population = settings.get('population')  # количество экземпляров популяции
g_x_range = settings.get('range')  # диапозон
g_mutation = settings.get('mutation')  # частота мутации
g_bit_size = settings.get('bit_size')  # колисчество первых битов числа
g_children_count = settings.get('child_count')  # количество потомков одной семьи
g_max_level_quality = settings.get('level_quality')  # максимальное количество повторений для остановки


def fitness_function(x: int) -> int:
    return -1 * (x - 6) * (x - 20) * (x - 38) * (x - 61)  # 12 вариант


points = generic_algorithm(
    population=g_population,
    x_range=g_x_range,
    bit_size=g_bit_size,
    children_count=g_children_count,
    mutation_probability=g_mutation,
    max_level_quality=g_max_level_quality,
    fitness_function=fitness_function
)

labels = []
for index in range(len(points)):
    labels.append(f"П {index}")

for i in range(len(points)):
    print(f'{labels[i]} : {points[i]}')

view(x_range=g_x_range, x_coords=points, labels=labels, function=fitness_function)


