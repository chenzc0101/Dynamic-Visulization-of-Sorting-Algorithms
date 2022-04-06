from graphics import *
import random

win = GraphWin('visual', 500, 500, autoflush=False)

def make_display_grid(rows, cols):
    # make a 2-D list of Rectangles with dimensions (rows x cols).
    displaygrid = [[None for j in range(cols)] for i in range(rows)]
    # use a nested for loop to set the location and color of each Rectangle.
    for i in range(rows):
        for j in range(cols):
            a = Rectangle(Point(10 * i, 10 * j), Point(10 * (i + 1), 10 * (j+1)))
            a.setFill('black')
            displaygrid[i][j] = a
            displaygrid[i][j].draw(win)
    return displaygrid

def list_generation(length):
#From Zichao Chen's code
    A = [x for x in range(length)]
    random.seed(time.time())
    random.shuffle(A)
    return A


def display(list, display_grid, redlist = []):
    # use a nested for loop to set the color of each Rectangle in display_grid so that it matches
    # the string in grid.
    r = [False for i in range(len(list))]
    for num in redlist:
        r[num] = True
    for i in range(len(display_grid)):
        for j in range(len(display_grid[0])):
            if list[i] == len(display_grid[0]) - j - 1:
                if r[i]:
                    display_grid[i][j].setFill('red')
                else:
                    display_grid[i][j].setFill('green')
            else:
                display_grid[i][j].setFill('black')
    update()


