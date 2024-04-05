# recieves a class which implements fitness and has a field called
# chromosomes
import random
#from Print_Graph import draw_combined_plot

class GenericEvoluion:
    def __init__(self, problem, num_of_gens, elitism):
        self.problem = problem
        self.num_of_gens = num_of_gens
        self.elitism = elitism
        self.maxFitness = []
        self.averageFitness = []
        self.l = 0

    def do_one_generation(self):
        # population = self.problem.population
        fitness = {}
        total = 0
        max_fitness = 0
        average_fitness = 0
        best_solution = []
        for chromosome in self.problem.chromosomes:
            cur_fitness = self.problem.fitness(chromosome)
            fitness[tuple(chromosome)] = cur_fitness
            total += cur_fitness
            if cur_fitness > max_fitness:
                best_solution = chromosome
                max_fitness = cur_fitness
            average_fitness += cur_fitness
        average_fitness /= len(self.problem.chromosomes)
        #print("average fitness is", average_fitness)
        #print("max fitness is", max_fitness)
        #print("best solution is", best_solution)
        #print("best solution cost is", self.problem.chromosomeCost(best_solution))
        if self.problem.fitness(best_solution) == self.problem.best_fitness:
            return best_solution
        # print("generation: ", self.l)
        self.maxFitness.append((self.l, max_fitness))
        self.averageFitness.append((self.l, average_fitness))
        self.l += 1
        self.crossover(total, fitness)
        return best_solution

    def get_parent(self, fitness, number, chromosomes):
        for chromosome in chromosomes:
            if fitness[tuple(chromosome)] > number:
                return chromosome
            number -= fitness[tuple(chromosome)]
        return chromosomes[-1]

    def crossover(self, total, fitness):
        num_of_chromosomes = len(self.problem.chromosomes)
        fitness_range = total
        self.problem.chromosomes.sort(key=lambda chromosome: fitness[tuple(chromosome)], reverse=True)

        for i in range(self.elitism):
            fitness_range -= fitness[tuple(self.problem.chromosomes[-1])]
            # execute losers
            self.problem.chromosomes.pop()
        temp = self.problem.chromosomes.copy()
        self.problem.chromosomes = []
        for i in range(self.elitism):
            self.problem.chromosomes.append(temp[i])

        # do roulette and generate children
        for i in range((num_of_chromosomes - self.elitism) // 2):
            random_number = random.randint(0, total)
            parent1 = self.get_parent(fitness, random_number, temp)
            random_number = random.randint(0, total)
            parent2 = self.get_parent(fitness, random_number, temp)
            child1, child2 = self.problem.crossover(parent1, parent2)
            self.problem.chromosomes.append(child1)
            self.problem.chromosomes.append(child2)

    def run(self):
        for i in range(self.num_of_gens):
            print("generation is", i)
            best_solution = self.do_one_generation()
        if self.problem.id==1:
            best_solution = [0] + best_solution
            best_result=[]
            for num in best_solution:
                best_result.append(num + 1)
            print(best_result)
        '''
        file_name = "output.txt"
        # פתח את הקובץ לכתיבה
        with open(file_name, "w") as file:
            file.write(str(1) + "\n")

            # עבור על כל איבר במערך
            for item in best_solution:
                # כתוב את האיבר לקובץ, כל איבר בשורה נפרדת
                file.write(str(item + 1) + "\n")
            file.write(str(1) + "\n")

        draw_combined_plot(self.maxFitness, self.averageFitness)
        '''
