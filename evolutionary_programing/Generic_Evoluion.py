# recieves a class which implements fitness and has a field called
# chromosomes
import random
class Generic_Evoluion:
    def __init__(self, problem, num_of_gens, elitism):
        self.problem = problem
        self.num_of_gens = num_of_gens
        self.elitism = elitism

    def do_one_generation(self):
        population = self.problem.population
        fitness = {}
        total = 0
        for chromosome in self.problem.chromosomes:
            cur_fitness = self.problem.fitness(population)
            fitness[chromosome] = cur_fitness
            total += cur_fitness

    def crossover(self, total, fitness):
        num_of_chromosomes = len(self.problem.chromosomes)
        fitness_range = total
        self.problem.population.chromosomes.sort(key=lambda chromosome: fitness[chromosome])

        for i in range(self.elitism):
            fitness_range -= fitness[self.problem.chromosomes[-1]]
            # execute losers
            self.problem.chromosomes.pop()
        temp = self.problem.chromosomes.copy()
        self.problem.chromosomes.empty()
        for i in range(self.elitism):
            self.problem.chromosomes.append(temp[i])
        for i in range(num_of_chromosomes - self.elitism):
            random_number = random.randint(0, total)
