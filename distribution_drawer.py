import numpy as np
from matplotlib import pyplot as plt


def draw_distribution(name, result):
    plt.title(name)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.hist(result, bins=20)
    plt.show()

    print()
    print(name)
    mean = np.mean(result)
    variance = np.var(result)
    std_deviation = np.std(result)
    print(f"Математическое ожидание: {mean}")
    print(f"Дисперсия: {variance}")
    print(f"Среднее квадратичное отклонение: {std_deviation}")
    print()
