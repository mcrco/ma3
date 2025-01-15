import numba
import numpy as np

n_trials = int(1e8)


@numba.njit(parallel=True)
def p1a():
    numer = 0
    for _ in numba.prange(n_trials):
        deck = np.array([i // 4 for i in range(52)])
        np.random.shuffle(deck)
        count = 0
        for p in range(4):
            acount = 0
            kcount = 0
            for card in deck[p * 13 : (p + 1) * 13]:
                if card == 0:
                    acount += 1
                if card == 12:
                    kcount += 1
            if acount == 1 and kcount == 1:
                count += 1
        if count == 1:
            numer += 1
    print(numer / n_trials)


@numba.njit(parallel=True)
def p1b():
    numer = 0
    for _ in numba.prange(n_trials):
        deck = np.array([i // 4 for i in range(52)])
        np.random.shuffle(deck)
        acount = np.zeros(2, dtype=np.int32)
        for p in range(2):
            for card in deck[p * 13 : (p + 1) * 13]:
                if card == 0:
                    acount[p] += 1
        if acount[0] == 1 and acount[1] == 1:
            numer += 1
    print(numer / n_trials)


@numba.njit(parallel=True)
def p5():
    numer = 0
    for _ in numba.prange(n_trials):
        deck = np.array([i // 4 for i in range(52)])
        np.random.shuffle(deck)
        count = 0
        for p in range(3):
            hand = deck[p * 2 : (p + 1) * 2]
            if 0 in hand and (10 in hand or 12 in hand):
                count += 1
        if count >= 2:
            numer += 1
    print(numer / n_trials)


p1a()
p1b()
p5()
