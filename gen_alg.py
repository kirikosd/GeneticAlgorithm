from random import randint, choices, randrange
from create_graph import size, G

colors = ["B", "R", "G", "Y"]       # lista me ta diathesima xrwmata


def generate_genome():              # paragei tyxaies lyseis(chromoswmata)
    genome = []
    for _ in range(0, size):
        i = randint(0, 3)
        genome.append(colors[i])
    return genome


def generate_population():          # paragei ton arxiko plithismo
    pop = []                        # apo tyxaies lyseis
    for _ in range(0, size):
        i = generate_genome()
        pop.append(i)
    return pop


def fitness_function(genome):                           # ypologizei poso katallili einai kathe lisi
    fit_sum = 0                                         # Oso megalitero to fit_sum toso kaliteri h lisi
    for edge in G.edges:                                # Megisto fit_sum einai to 41 opou kai den xreiazetai
        if genome[edge[0]-1] != genome[edge[1]-1]:      # na synexisoyme
            fit_sum += 1
    return fit_sum


def population_fitness(pop):                            # epistrefei mia lista me thn katallilotita
    pop_sum = []                                        # kathe lisis toy plithismou
    for i in pop:
        pop_sum.append(fitness_function(i))
    return pop_sum


def single_point_crossover(gen_a, gen_b):               # diastayrwsh enos shmeiou
    p = randint(0, 15)
    return gen_a[0:p] + gen_b[p:], gen_b[0:p] + gen_a[p:]


def selection_pair(pop):                                # dialegei tous goneis tyxaia me bash tis pithanothtes
    return choices(pop, weights=[fitness_function(gene) for gene in pop], k=2)


def mutation(genome, clr):                              # metallasei ta chromoswmata
    index = randrange(len(genome))
    genome[index] = clr[randint(0, 3)]
    return genome


def run():
    temp = False
    fitness_limit = 41
    generation_limit = 150
    population = generate_population()
    for i in range(generation_limit):
        population.sort(key=fitness_function, reverse=True)     # taksinomei tis liseis me vash thn
        pop_fitness = population_fitness(population)            # katallilothta tous
        pop_fitness.sort(reverse=True)

        print(f"Generation:{i}")                                # ektypwnei statistika
        for k in range(len(population)):
            print(population[k], pop_fitness[k])
        print("-----------------------------------------------------------------------------------")

        if pop_fitness[0] == fitness_limit:                     # elegxei an vrethike h teleia lisi
            temp = True
            break

        next_gen = population[0:2]

        for j in range(int(len(population) / 2) - 1):           # paragei ton neo plithismo
            parents = selection_pair(population)
            offspring_a, offspring_b = single_point_crossover(parents[0], parents[1])
            offspring_a = mutation(offspring_a, colors)
            offspring_b = mutation(offspring_b, colors)
            next_gen += [offspring_a, offspring_b]

        population = next_gen

    return population[0], i, temp
