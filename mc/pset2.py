import numba
import numpy as np

n_trials = int(1e8)


@numba.njit(parallel=True)
def p2():
    numer = 0
    for i in ra
