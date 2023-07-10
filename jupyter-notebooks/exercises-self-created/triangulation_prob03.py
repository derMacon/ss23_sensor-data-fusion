import numpy as np


# see problem 03 from exercises (not homeworks)


def triangular_calc(d):
    d = np.array(d)

    a = d[:, 2]
    p = np.array([d[:, 0], d[:, 1]]).T

    y = p[:, 0] * np.tan(a) - p[:, 1]
    H = np.array([np.tan(a), np.full(a.shape[0], -1)]).T

    print('a: ', a)
    print('p: ', p)
    print('H: ', H)
    print('y: ', y)

    x_ls = np.linalg.inv(H.T @ H) @ H.T @ y

    print('x_ls: ', x_ls)

    return x_ls


d = [
    [0, 0, np.pi / 4],
    [4, 0, 3 * np.pi / 4],
    [0, 2.5, 0],
]

x_ls = triangular_calc(d)
