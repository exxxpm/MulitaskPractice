from multiprocessing import Pool
import random
import math


def compute_pi_estimate(num_samples):
    count_inside = 0
    for _ in range(num_samples):
        x = random.random()
        y = random.random()
        if math.sqrt(x ** 2 + y ** 2) < 1:
            count_inside += 1
    return 4 * (count_inside / num_samples)


if __name__ == '__main__':
    with Pool(5) as pool:
        results = pool.map(compute_pi_estimate, [1000, 10000, 100000, 1000000, 10000000])

    for result in results:
        print(f"{result:.7f}")
