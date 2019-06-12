#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.


def queensAttack(n, k, r_q, c_q, obstacles):
    right = [r_q, n+1]
    left = [r_q, 0]
    down = [0, c_q]
    up = [n+1, c_q]
    if r_q > c_q:
        r_u = [n+1, c_q + n + 1 - r_q]
        l_d = [r_q - c_q,0]
    else:
        r_u = [r_q + n + 1 - c_q, n+1]
        l_d = [0, c_q - r_q]

    if r_q > (n + 1 - c_q):
        r_d = [r_q + c_q - n - 1,n+1]
        l_u = [n+1, r_q + c_q - n - 1]
    else:
        r_d = [0, c_q + r_q]
        l_u = [r_q + c_q, 0]

    for i in obstacles:
        if i[0] == r_q and c_q < i[1] < right[1]:
            right = i
        elif i[0] == r_q and c_q > i[1] > left[1]:
            left = i
        elif i[1] == c_q and r_q < i[0] < up[0]:
            up = i
        elif i[1] == c_q and r_q > i[0] > down[0]:
            down = i
        elif (i[0] - r_q) / (i[1] - c_q) == 1.0 and r_q < i[0] < r_u[0]:
            r_u = i
        elif (i[0] - r_q) / (i[1] - c_q) == 1.0 and r_q > i[0] > l_d[0]:
            l_d = i
        elif (i[0] - r_q) / (i[1] - c_q) == -1.0 and r_q < i[0] < l_u[0]:
            l_u = i
        elif (i[0] - r_q) / (i[1] - c_q) == -1.0 and r_q > i[0] > r_d[0]:
            r_d = i
    number_steps = up[0] - down[0] + right[1] - left[1] + r_u[0] - l_d[0] + l_u[0] - r_d[0] - 8
    return number_steps

nk = input().split()

n = int(nk[0])

k = int(nk[1])

r_qC_q = input().split()

r_q = int(r_qC_q[0])

c_q = int(r_qC_q[1])

obstacles = []

for _ in range(k):
    obstacles.append(list(map(int, input().rstrip().split())))

result = queensAttack(n, k, r_q, c_q, obstacles)

print(str(result) + '\n')

