from Generic_Evoluion import GenericEvoluion
import random
import time
import math


def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

def read_from_data(name):
    with open(name, 'r') as file:
        # קרוא את התוכן של הקובץ
        lines = file.readlines()

        # יצירת מערך של טאפלים
        tuples_array = []

        # לולאה על כל שורה בקובץ
        for line in lines:
            # פיצוץ השורה למספרים
            numbers = [int(num) for num in line.split()]

            # יצירת טאפל והוספתו למערך
            tuple_item = (numbers[0], numbers[1])
            tuples_array.append(tuple_item)
        return tuples_array


def maxPath(matrix):
    max_element = matrix[0][0]

    for row in matrix:
        for element in row:
            if element > max_element:
                max_element = element

    return max_element * len(matrix[0])


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
        print(self.distanceMatrix)
        self.maxPath = maxPath(self.distanceMatrix)
        self.homeCity = array_index[0]  # put the home city

    def chromosomeCost(self, chromosome):
        sumPath = 0
        for i in range(len(chromosome) - 1):
            sumPath += self.distanceMatrix[chromosome[i]][chromosome[i + 1]]
        sumPath += self.distanceMatrix[0][chromosome[0]]
        sumPath += self.distanceMatrix[chromosome[-1]][0]
        return sumPath

    def fitness(self, chromosome):

        return round((self.maxPath - self.chromosomeCost(chromosome)))

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
                child1.append(city)
        for city in parent1:
            if city not in child2:
                child2.append(city)
        return child1, child2


if __name__ == "__main__":
    start_time = time.time()

    traveler = Traveling_Salesman_Evoluion(300, 0.1, read_from_data('tsp.txt'))

    solution = GenericEvoluion(traveler, 5000, 2)
    solution.run()
    end_time = time.time()
    elapsed_time_minutes = (end_time - start_time) / 60

    # הדפס את תוצאת הקוד ואת זמן הריצה
    print(f"זמן ריצה: {elapsed_time_minutes:.4f} דקות")
