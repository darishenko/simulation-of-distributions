import array
import random


def calculate_current_r(a, m, previous_r):
    return divmod(a * previous_r, m)[1]


def get_sequence_item(item, m):
    return item / m


def create_sequence(a, m, r0, N):
    r0, a, m = random_init_values()
    result = array.array('f')
    iter_number = 0
    while iter_number < N:
        r0 = calculate_current_r(a, m, r0)
        result.append(get_sequence_item(r0, m))
        iter_number += 1
    return result


def random_init_values():
    r0 = random.randint(2, 100)
    a = random.randint(1000, 5000)
    m = random.randint(10000000, 20000000)
    return r0, a, m
