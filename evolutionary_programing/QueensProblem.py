import random

from Generic_Evoluion import GenericEvoluion


class Queens_Evoluion:
    def generateSolution(self):
        solution = [1, 2, 3, 4, 5, 6, 7, 8]
        random.shuffle(solution)
        return solution

    def create_first_gen(self):
        for i in range(self.num_of_chromosomes):
            self.chromosomes.append(self.generateSolution())

    def __init__(self, num_of_chromosomes, mutation_rate):
        self.chromosomes = []
        self.num_of_chromosomes = num_of_chromosomes
        self.create_first_gen()
        self.mutation_rate = 0.01  # mutation_rate

    def fitness(self, chromosome):
        fitness = 0
        for i in range(8):
            for j in range(i + 1, 8):
                if chromosome[i] != chromosome[j] and abs(i - j) != abs(chromosome[i] - chromosome[j]):
                    fitness += 1
        return fitness

    def mutate(self, chromosome):
        pos1, pos2 = random.sample(range(8), 2)
        temp = chromosome[pos1]
        chromosome[pos1] = chromosome[pos2]
        chromosome[pos2] = temp
        # return chromosome

    def crossover(self, parent1, parent2):
        child1 = []
        child2 = []
        crossover_point = random.randint(0, 7)
        for i in range(8):
            if i > crossover_point:
                child1.append(parent1[i])
                child2.append(parent2[i])
            else:
                child2.append(parent1[i])
                child1.append(parent2[i])
        return child1, child2


if __name__ == "__main__":
    queens = Queens_Evoluion(200, 0.1)
    solution = GenericEvoluion(queens, 200, 2)
    solution.run()
