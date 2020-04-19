
import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    pre = [     [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
                [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
                [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
                [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
                [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
                [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
                [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
                [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
                ]

    t = []
    for i in pre:
        res = 0
        for j,k in zip(i,s):
            for x,y in zip(j,k):
                res+= max([x,y]) - min([x,y])
        t.append(res)
    print(min(t))
if __name__ == '__main__':
    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

