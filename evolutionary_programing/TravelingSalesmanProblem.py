from Generic_Evoluion import GenericEvoluion
import random

import math


def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


class Traveling_Salesman_Evoluion:

    def createDistanceMatrix(self, arrayIndex):
        matrix = [[0] * len(arrayIndex) for _ in range(len(arrayIndex))]
        for i in range(0, len(arrayIndex)):
            for j in range(len(arrayIndex)):
                matrix[i][j] = euclidean_distance(arrayIndex[i], arrayIndex[j])

        return matrix

    def generateSolution(self):
        solution = []
        for i in range(1, self.num_of_cities + 1):
            solution.append(i)
        random.shuffle(solution)
        return solution

    def create_first_gen(self):
        for i in range(self.num_of_chromosomes):
            self.chromosomes.append(self.generateSolution())

    def __init__(self, num_of_chromosomes, mutation_rate, array_index):
        self.chromosomes = []
        self.num_of_chromosomes = num_of_chromosomes
        self.num_of_cities = len(array_index) - 1
        self.create_first_gen()
        self.mutation_rate = mutation_rate  # mutation_rate
        self.distanceMatrix = self.createDistanceMatrix(array_index)  # put the distanceMatrix
        self.homeCity = array_index[0]  # put the home city

    def fitness(self, chromosome):
        fitness = 0
        for i in range(len(chromosome) - 1):
            fitness += self.distanceMatrix[i][i + 1]
        fitness += self.distanceMatrix[0][chromosome[0]]
        fitness += self.distanceMatrix[chromosome[-1]][0]
        return fitness

    def mutate(self, chromosome):
        index1, index2 = random.sample(range(len(chromosome)), 2)
        chromosome[index1], chromosome[index2] = chromosome[index2], chromosome[index1]
        return chromosome

    def crossover(self, parent1, parent2):
        crossover_point = random.randint(0, len(parent1) - 1)
        child1 = parent1[0:crossover_point]
        child2 = parent2[0:crossover_point]
        for city in parent2:
            if city not in child1:
                child1.appand(city)
        for city in parent1:
            if city not in child2:
                child2.appand(city)
        return child1, child2
