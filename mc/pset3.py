import numpy as np
import numba
import random

N_TRIALS = int(1e8)


@numba.njit(parallel=True)
def p2():
    # part a
    dice = np.array([1, 2, 3, 4, 5, 6])
    rolls = np.random.choice(dice, size=N_TRIALS)
    print("Expected value of dice roll:", int(np.sum(rolls)) / N_TRIALS)

    # part b
    rolls = np.random.choice(dice, size=(N_TRIALS, 4))
    sums = np.sum(rolls, axis=1)
    print("Expected value of 4 dice rolls:", int(np.sum(sums)) / N_TRIALS)


@numba.njit(parallel=True)
def p3():
    games = np.zeros(N_TRIALS)
    for t in numba.prange(N_TRIALS):
        wins = [0, 0]
        for g in range(7):
            wins[random.getrandbits(1)] += 1
            if wins[0] == 4 or wins[1] == 4:
                games[t] = g + 1
                break
    mean = np.mean(games)
    stdev = np.std(games)
    print("Expected value of games played:", mean)
    print("Variance of games played:", stdev)


@numba.njit(parallel=True)
def p5():
    count = 0
    for _ in numba.prange(N_TRIALS):
        outcomes = np.random.uniform(low=0.0, high=1.0, size=110)
        outcomes = np.where(outcomes < 0.1, 0, 1)
        if np.sum(outcomes) <= 100:
            count += 1
    print("Probability that there are enough seats:", count / N_TRIALS)


if __name__ == "__main__":
    p2()
    p3()
    p5()
