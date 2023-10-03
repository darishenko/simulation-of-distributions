import generator
from distribution_drawer import draw_distribution
from sequence_simulator import simulate_uniform_distribution, simulate_exponential_distribution, \
    simulate_gamma_distribution, simulate_normal_distribution, \
    simulate_simpson_distribution, simulate_triangular_distribution_max, \
    simulate_triangular_distribution_min

N = 100_000

if __name__ == '__main__':
    arr = generator.create_sequence(100_057, 301_181, 500_089, N)
    result = simulate_uniform_distribution(2, 5, N, arr)
    draw_distribution('равномерное распределение', result)

    result = simulate_normal_distribution(3, 1, N)
    draw_distribution('гауссовское (нормальное) распределение', result)

    result = simulate_exponential_distribution(2, N)
    draw_distribution('экспоненциальное распределение', result)

    result = simulate_gamma_distribution(1, 6, N)
    draw_distribution('гамма распределение', result)

    result = simulate_triangular_distribution_max(-4, 5, N)
    draw_distribution('треугольное распределение', result)
    result = simulate_triangular_distribution_min(-4, 5, N)
    draw_distribution('треугольное распределение', result)

    result = simulate_simpson_distribution(4, 8, N)
    draw_distribution('распределение симпсона', result)
