import math
import random
import time
from Generic_Evoluion import GenericEvoluion


def is_safe(board, row, col):
    # Check if there is any queen in the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, 8, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_queens_util(board, col):
    if col >= 8:
        return True

    for i in range(8):
        if is_safe(board, i, col):
            board[i][col] = 1

            if solve_queens_util(board, col + 1):
                return True

            board[i][col] = 0

    return False


def solve_queens():
    board = [[0] * 8 for _ in range(8)]

    if not solve_queens_util(board, 0):
        print("Solution does not exist")
        return False

    print("Solution exists:")
    for row in board:
        print(row)

    return True


# Solve the problem
solve_queens()


class Queens_Evoluion:
    def generateSolution(self):
        solution = [1, 2, 3, 4, 5, 6, 7, 8]
        random.shuffle(solution)
        while self.fitness(solution) > 24:
            random.shuffle(solution)
        return solution

    def create_first_gen(self):
        for i in range(self.num_of_chromosomes):
            self.chromosomes.append(self.generateSolution())

    def __init__(self, num_of_chromosomes, mutation_rate):
        self.chromosomes = []
        self.num_of_chromosomes = num_of_chromosomes
        self.create_first_gen()
        self.mutation_rate = mutation_rate  # mutation_rate
        self.best_fitness = 28

    def fitness(self, chromosome):
        fitness = 0
        for i in range(8):
            for j in range(i + 1, 8):
                if chromosome[i] != chromosome[j] and abs(i - j) != abs(chromosome[i] - chromosome[j]):
                    fitness += 1
        # return math.ceil(math.sqrt(fitness))
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
        res1 = random.random()
        res2 = random.random()
        if res1 < self.mutation_rate:
            self.mutate(child1)
        if res2 < self.mutation_rate:
            self.mutate(child2)
        return child1, child2

    def brute_force(self):
        for i in range(1,9):
            for j in range(1,9):
                for k in range(1,9):
                    for l in range(1,9):
                        for r in range(1,9):
                            for c in range(1,9):
                                for d in range(1,9):
                                    for e in range(1,9):
                                        lst = [i, j, k, l, r, c, d, e]
                                        if self.fitness(lst) == 28:
                                            return lst


if __name__ == "__main__":
    start_time = time.time()
    # Calculate running time
    queens = Queens_Evoluion(200, 0.05)
    solution = GenericEvoluion(queens, 300, 2)
    solution.run()
    end_time = time.time()
    running_time = end_time - start_time
    print("Running time of genetic: " + str(running_time))
    # Convert inner lists to tuples before adding to set
    based = []
    almost = []
    for row in queens.chromosomes:
        if queens.fitness(row) == 28:
            based.append(row)
        if queens.fitness(row) == 27:
            almost.append(row)
    print(set(tuple(row) for row in based))
    print(set(tuple(row) for row in almost))
    #start_time = time.time()
    #bf_solution = queens.brute_force()
    #end_time = time.time()
    #running_time = end_time - start_time
    #print("Running time of brute force is", running_time)
    #print("brute foce solution is ", bf_solution)
    # solve_queens()
