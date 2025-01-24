import numpy as np
import numba
import random

N_TRIALS = int(1e6)


@numba.njit(parallel=True)
def p2():
    # part a
    dice = np.array([1, 2, 3, 4, 5, 6])
    rolls = np.random.choice(dice, size=N_TRIALS)
    print(f"Expected value of dice roll: {np.sum(rolls) / N_TRIALS}")

    # part b
    rolls = np.random.choice(dice, size=(N_TRIALS, 4))
    sums = np.sum(rolls, axis=1)
    print(f"Expected value of 4 dice rolls: {np.sum(sums) / N_TRIALS}")


@numba.njit(parallel=True)
def p3():
    games = []
    for _ in numba.prange(N_TRIALS):
        wins = [0, 0]
        for g in range(7):
            wins[random.getrandbits(1)] += 1
            if wins[0] == 4 or wins[1] == 4:
                games.append(g + 1)
    games = np.array(games)
    mean = np.mean(games)
    stdev = np.std(games)
    print(f"Expected value of games played: {mean}")
    print(f"Variance of games played: {stdev}")


@numba.njit(parallel=True)
def p5():


p2()
p3()
