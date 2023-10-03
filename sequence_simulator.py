import math
from array import array

import generator

A = 100_057
M = 301_181
R0 = 500_089

NORMAL_D_SUMM_COUNT = 6


def simulate_uniform_distribution(a, b, N, arr):
    result = array('f')
    for ind in range(N):
        result.append(a + (b - a) * arr[ind])
    return result


def simulate_normal_distribution(m_x, si_x, N):
    result = array('f')
    arr = generator.create_sequence(A, M, 3, N * NORMAL_D_SUMM_COUNT)
    for ind in range(N):
        value = 0
        for j in range(NORMAL_D_SUMM_COUNT):
            g = ind * NORMAL_D_SUMM_COUNT + j
            value += arr[g]
        result.append(m_x + si_x * math.sqrt(2) * (value - 3))
    return result


def simulate_exponential_distribution(y, N):
    result = array('f')
    arr = generator.create_sequence(100_057, 301_181, 3, N)
    for ind in range(N):
        result.append(- (1 / y) * math.log(arr[ind], math.e))
    return result


def simulate_gamma_distribution(y, nu, N):
    result = array('f')
    nu = math.ceil(nu)
    arr = generator.create_sequence(100_057, 301_181, 5, nu * N)
    for ind in range(N):
        value = 1
        for j in range(nu):
            value *= arr[ind * nu + j]
        gamma_value = -(1 / y) * math.log(value)
        result.append(gamma_value)
    return result


def simulate_triangular_distribution_max(a, b, N):
    result = []
    arr1 = generator.create_sequence(3, 209715120, 7, N)
    arr2 = generator.create_sequence(100_057, 301_181, 500_089, N)
    for ind in range(N):
        value = a + (b - a) * max(arr1[ind], arr2[ind])
        result.append(value)
    return result


def simulate_triangular_distribution_min(a, b, N):
    result = []
    arr1 = generator.create_sequence(3, 209715120, 7, N)
    arr2 = generator.create_sequence(100_057, 301_181, 500_089, N)
    for ind in range(N):
        value = a + (b - a) * min(arr1[ind], arr2[ind])
        result.append(value)
    return result


def simulate_simpson_distribution(a, b, N):
    result = array('f')
    arr1 = generator.create_sequence(3, 209715120, 7, N)
    arr2 = generator.create_sequence(100_057, 301_181, 500_089, N)
    arr1 = simulate_uniform_distribution(a / 2, b / 2, N, arr1)
    arr2 = simulate_uniform_distribution(a / 2, b / 2, N, arr2)
    for ind in range(N):
        result.append(arr1[ind] + arr2[ind])
    return result
