
import random


# Функция для создания случайной популяции
def create_population(population_size, chromosome_length):
    population = []
    for _ in range(population_size):
        chromosome = [random.randint(0, 1) for _ in range(chromosome_length)]
        population.append(chromosome)
    return population


# Функция для вычисления пригодности (fitness) каждого хромосомы
def calculate_fitness(chromosome):
    # Здесь нужно реализовать вашу функцию оценки пригодности
    # Чем лучше хромосома, тем больше значение fitness
    return sum(chromosome)


# Функция для выбора родителей на основе рулеточного отбора
def select_parents(population, fitness_values):
    total_fitness = sum(fitness_values)
    probabilities = [fitness / total_fitness for fitness in fitness_values]
    parents = random.choices(population, probabilities, k=2)
    return parents


# Функция для скрещивания двух родителей и создания потомка
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child


# Функция для мутации потомка
def mutate(chromosome, mutation_rate):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = 1 - chromosome[i]
    return chromosome


# Генетический алгоритм
def genetic_algorithm(population_size, chromosome_length, generations, mutation_rate):
    population = create_population(population_size, chromosome_length)

    for _ in range(generations):
        fitness_values = [calculate_fitness(chromosome) for chromosome in population]

        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = select_parents(population, fitness_values)
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            new_population.extend([child1, child2])

        population = new_population

    best_chromosome = max(population, key=calculate_fitness)
    best_fitness = calculate_fitness(best_chromosome)

    return best_chromosome, best_fitness


# Пример использования генетического алгоритма
population_size = 100
chromosome_length = 10
generations = 100
mutation_rate = 0.01

best_chromosome, best_fitness = genetic_algorithm(population_size, chromosome_length, generations, mutation_rate)

print("Best chromosome:", best_chromosome)
print("Best fitness:", best_fitness)
