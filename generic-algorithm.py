import random

from settings import Settings

settings = Settings()
# logger = Logger('report_', '.txt')

g_population = settings.get('population')  # количество экземпляров популяции
g_x_range = settings.get('range')  # диапозон
g_mutation = settings.get('mutation')  # частота мутации
g_bit_size = settings.get('bit_size')  # колисчество первых битов числа
g_children_count = settings.get('child_count')  # количество потомков одной семьи
g_max_level_quality = settings.get('level_quality')  # максимальное количество повторений для остановки


def fitness_function(x: int) -> int:
    return -1 * (x - 6) * (x - 20) * (x - 38) * (x - 61)  # 12 вариант


def get_max_value_function(function, x_range) -> tuple[int, int]:
    max_value = function(x_range[0])
    max_index = x_range[0]
    for i in range(x_range[0] + 1, x_range[1]):
        value = function(i)
        if max_value < value:
            max_value = value
            max_index = i
    return max_value, max_index


def get_bits(num: int, bit_size: int) -> str:
    return bin(num).split('b')[1][:bit_size].rjust(bit_size, '0')


def get_int(bites: str) -> int:
    return int(bites, 2)


def randrange(start: int, stop: int, exclude_list=None) -> int:
    if exclude_list is None:
        exclude_list = []
    exclude = set(exclude_list)
    rand_num = random.randrange(start=start, stop=stop)
    while rand_num in exclude:
        rand_num = random.randrange(start=start, stop=stop)
    return rand_num


def generate_parents(population: int, x_range: list[int], bit_size: int) -> list[str]:
    parents = []
    for i in range(population):
        x = fitness_function(x=randrange(*x_range))
        parents.append(get_bits(num=x, bit_size=bit_size))
    return parents


def create_families(parents: list[str]) -> list[tuple[str, str]]:
    families = []
    exclude_list = []
    parents_count = len(parents)
    max_families_count = parents_count // 2
    create_families_count = 0

    def get_parent() -> str:
        index = randrange(0, parents_count, exclude_list)
        exclude_list.append(index)
        return parents[index]

    while create_families_count < max_families_count:
        families.append((get_parent(), get_parent()))
        create_families_count += 1

    return families


def crossing(families: list[tuple[str, str]], child_count: int) -> list[str]:
    children = []
    bit_size = len(families[0][0])
    for family in families:
        for i in range(child_count):
            position = randrange(1, bit_size)
            child = family[0][:position] + family[1][position:]
            children.append(child)
    return children


def mutation(children: list[str], mutation_probability: float):
    copy_children = children[:]

    if random.random() < mutation_probability:
        child_index = randrange(0, len(children))
        mutation_index = randrange(1, len(children[0]))
        child = copy_children[child_index]
        new_gene = '1' if child[mutation_index] == '0' else '0'
        child = child[:mutation_index] + new_gene + child[mutation_index + 1:]
        copy_children[child_index] = child

    return copy_children


def extension_population(parents: list[str], children: list[str]) -> list[str]:
    return parents + children


def decline_population(parents: list[str], population: int) -> list[str]:
    return sorted(parents.copy(), key=lambda x: fitness_function(get_int(x)), reverse=True)[:population]


def is_equals_to(x_value: int, parents: list[str]) -> bool:
    for parent in parents:
        if get_int(parent) != x_value:
            return False
    return True


def generic_algorithm() -> list[list[int]]:
    max_value = get_max_value_function(fitness_function, g_x_range)[1]
    recent_level_quality = 0
    real_x_value = None
    history = []

    parents = generate_parents(g_population, g_x_range, g_bit_size)
    history.append([get_int(x) for x in parents])

    while True:
        families = create_families(parents)
        children = crossing(families, g_children_count)
        children = mutation(children, g_mutation)
        parents = extension_population(parents, children)
        parents = decline_population(parents, g_population)

        history.append([get_int(x) for x in parents])

        if is_equals_to(max_value, parents):
            print("stop by max value")
            return history

        if real_x_value != get_int(parents[0]):
            real_x_value = get_int(parents[0])
            recent_level_quality = 0
        if is_equals_to(real_x_value, parents):
            recent_level_quality += 1
        if recent_level_quality == g_max_level_quality:
            print("stop by level quality")
            return history


history = generic_algorithm()
print(history)