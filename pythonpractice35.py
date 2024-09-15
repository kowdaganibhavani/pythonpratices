import time

def sums(n):

    star= time.time()

    s = 0
    for i in range(1, n + 1):
        s = s + i

    end_time = time.time()

    return s, end_time - star

n = 5

print("\nTime to sum of 1 to", n, "and calculate is:", sum_of_n_numbers(n))