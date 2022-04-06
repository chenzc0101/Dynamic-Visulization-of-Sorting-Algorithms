import visualization
from graphics import *
def PARTITION(A, p, r, display_grid):
    # Complete the code here, see README on course website for problem description and instructions.
    x = A[r-1]
    i = p - 1
    for j in range(p,r - 1):
        if A[j] <= x:
            i += 1
            visualization.display(A, display_grid, [i,j])
            y = A[i]
            A[i] = A[j]
            A[j] = y
            visualization.display(A, display_grid, [i,j])
    visualization.display(A, display_grid, [i+1,r-1])
    y = A[i + 1]
    A[i + 1] = A[r - 1]
    A[r - 1] = y
    visualization.display(A, display_grid, [i+1,r-1])
    return i + 1





def QUICKSORT(A, p, r, display_grid):


    # Complete the code here, see README on course website for problem description and instructions.
    if p < r - 1:
        q = PARTITION(A, p, r, display_grid)
        QUICKSORT(A, p, q, display_grid)
        QUICKSORT(A, q + 1, r, display_grid)
    return


A = visualization.list_generation(50)

display_grid = visualization.make_display_grid(50,50)

QUICKSORT(A, 0, len(A), display_grid)