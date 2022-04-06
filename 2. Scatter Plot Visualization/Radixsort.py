#
# Created by Jiang Long 
#
# DKU CS301 FALL 2021 SESSION 02
#

import math, random, visualization

def RADIX_SORT(A, r, d):
    # d: number of digits
    # r: radix in number of r binary bits
    
    
    # In each iteration of the COUNTING_SORT_on_radix, you should use
    # the following to print out the Array after the re-arrangement:
    
    # for i in range(d): 
    #    .... call COUNTING_SORT_on_radix
    #    Stats.PrintArray(A, 'iter %s'%i)
    
    # Complete the code here, see README on course website for problem description and instructions.
    for i in range(d):
        A = COUNTING_SORT_on_radix(A, r, i)



    return A


def COUNTING_SORT_on_radix(A, r, i_th):

    # r is the number of binary bits in the radix
    # i_th `digit`
    # return array B which is sorted on the i_th 'digit' base on radix 2^r

    # Complete the code here, see README on course website for problem description and instructions.
    C = [0 for i in range(1<<(r*(i_th+1)))]
    D = [(A[j])&((1<<(r*(i_th+1))) -1) for j in range(len(A))]
    B = [None for i in range(len(A))]
    visualization.display(A, display_grid)
    for j in range(len(A)):
        C[D[j]] += 1
        visualization.display(A, display_grid, [j])
    for i in range(1, len(C)):
        C[i] = C[i] + C[i-1]
    for j in range(len(A)-1, -1, -1):
        B[C[D[j]] - 1] = A[j]
        C[D[j]] -= 1
    visualization.display(B, display_grid, [i for i in range(len(B))])




    return B

A = visualization.list_generation(50)

display_grid = visualization.make_display_grid(50,50)

RADIX_SORT(A, 1, 6)