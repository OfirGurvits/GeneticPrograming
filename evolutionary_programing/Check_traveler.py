import itertools
import math


def createDistanceMatrix(arrayIndex):
    matrix = [[0] * len(arrayIndex) for _ in range(len(arrayIndex))]
    for i in range(0, len(arrayIndex)):
        for j in range(len(arrayIndex)):
            matrix[i][j] = euclidean_distance(arrayIndex[i], arrayIndex[j])

    return matrix


def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


def calculate_distance(route, distances):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distances[route[i]][route[i + 1]]
    total_distance += distances[0][route[0]]
    total_distance += distances[route[-1]][0]
    return total_distance


def brute_force_tsp(cities):
    distances = createDistanceMatrix(cities)
    print(distances)
    num_cities = len(distances)
    print(num_cities)

    all_routes = list(itertools.permutations(range(1, num_cities)))
    min_distance = float('inf')
    optimal_route = None

    for route in all_routes:
        distance = calculate_distance(route, distances)
        if distance < min_distance:
            min_distance = distance
            optimal_route = route
    print("check- [1, 4, 6, 3, 2, 5]", calculate_distance([1, 4, 6, 3, 2, 5], distances))

    return optimal_route, min_distance


# Example usage:
# Replace 'cities' with the actual array of city coordinates (tuples)
if __name__ == "__main__":
    cities = [(8, 1), (7, 5), (1, 9), (5, 9), (0, 6), (8, 1), (0, 2)]

    optimal_route, min_distance = brute_force_tsp(cities)

    print("Optimal Route:", optimal_route)
    print("Minimum Distance:", min_distance)
