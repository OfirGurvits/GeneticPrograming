import matplotlib.pyplot as plt

def draw_combined_plot(points1, points2):
    # פרק את הנקודות לרשימות נפרדות של x ו-y
    x_values1 = [point[0] for point in points1]
    y_values1 = [point[1] for point in points1]

    x_values2 = [point[0] for point in points2]
    y_values2 = [point[1] for point in points2]

    # יצירת גרף קווים עבור שתי קבוצות הנקודות
    plt.plot(x_values1, y_values1, marker='o', linestyle='-', color='blue', label='max fitness')
    plt.plot(x_values2, y_values2, marker='o', linestyle='-', color='red', label='average fitness')

    # יצירת נקודות סקטר עבור שתי קבוצות הנקודות
    plt.scatter(x_values1, y_values1, color='blue', marker='o')
    plt.scatter(x_values2, y_values2, color='red', marker='o')

    # הגדרות נוספות לגרף
    plt.title('max fitness and average fitness per generation')
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.legend()

    # הצגת הגרף
    plt.show()
