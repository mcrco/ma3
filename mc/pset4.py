import math


def p1a():
    n = 9000
    p = 0.0005
    q = 1 - 0.0005
    p_0 = q**n
    p_1 = (1 / (1 * q)) * (n - 1 + 1) * p * p_0
    p_2 = (1 / (2 * q)) * (n - 2 + 1) * p * p_1
    p_3 = (1 / (3 * q)) * (n - 3 + 1) * p * p_2
    p_4 = (1 / (4 * q)) * (n - 4 + 1) * p * p_3

    # Compute cumulative probability P(X ≤ 4)
    P_X_leq_4 = p_0 + p_1 + p_2 + p_3 + p_4

    print(P_X_leq_4)


def p1b():
    lam = 4.5
    p_0 = math.exp(-lam)
    p_1 = lam / 1 * p_0
    p_2 = lam / 2 * p_1
    p_3 = lam / 3 * p_2
    p_4 = lam / 4 * p_3

    # Compute cumulative probability P(X ≤ 4)
    P_X_leq_4 = p_0 + p_1 + p_2 + p_3 + p_4

    print(P_X_leq_4)


if __name__ == "__main__":
    p1a()
    p1b()
