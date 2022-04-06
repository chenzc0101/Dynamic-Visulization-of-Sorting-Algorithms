
# DKU CS301 BK-Presentation: Zichao Chen, Ziqiao Ao, Zhiyun Lu
# Title: Dynamic Visualization of Sorting Algorithms

## Part1: Bar chart visualization using matplotlib
### Thanks to the instruction guideline from Najam R. Syed from https://nrsyed.com/.

import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def swap(A, i, j):

    if i != j:
        A[i], A[j] = A[j], A[i]

#The instruction about how to use "yield" in python can be found on Google.
#"Yield" is a very useful and convenience method in this project.

def insertionsort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1

        while j >= 0 and key < A[j]:
            swap(A, j+1, j)
            j = j - 1
            yield A

def bubblesort(A):

    if len(A) == 1:
        return

    swapped = True
    for i in range(len(A) - 1):
        if not swapped:
            break
        swapped = False
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)
                swapped = True
            yield A


def mergesort(A, start, end):

    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1
    yield from mergesort(A, start, mid)
    yield from mergesort(A, mid + 1, end)
    yield from merge(A, start, mid, end)
    yield A


def merge(A, start, mid, end):

    merged = []
    leftIdx = start
    rightIdx = mid + 1

    while leftIdx <= mid and rightIdx <= end:
        if A[leftIdx] < A[rightIdx]:
            merged.append(A[leftIdx])
            leftIdx += 1
        else:
            merged.append(A[rightIdx])
            rightIdx += 1

    while leftIdx <= mid:
        merged.append(A[leftIdx])
        leftIdx += 1

    while rightIdx <= end:
        merged.append(A[rightIdx])
        rightIdx += 1

    for i, sorted_val in enumerate(merged):
        A[start + i] = sorted_val
        yield A


def quicksort(A, start, end):

    if start >= end:
        return

    pivot = A[end]
    pivotIdx = start

    for i in range(start, end):
        if A[i] < pivot:
            swap(A, i, pivotIdx)
            pivotIdx += 1
        yield A
    swap(A, end, pivotIdx)
    yield A

    yield from quicksort(A, start, pivotIdx - 1)
    yield from quicksort(A, pivotIdx + 1, end)


def selectionsort(A):

    if len(A) == 1:
        return

    for i in range(len(A)):
        # Find minimum unsorted value.
        minVal = A[i]
        minIdx = i
        for j in range(i, len(A)):
            if A[j] < minVal:
                minVal = A[j]
                minIdx = j
            yield A
        swap(A, i, minIdx)
        yield A


if __name__ == "__main__":

    N = int(input("How many numbers do you want? --Please type here"))

    method_msg = "Choose a sorting method:\n(b)ubble\n(i)nsertion\n(m)erge \
        \n(q)uick\n"
    method = input(method_msg)

# This step is used to randomly generate N numbers in a list

    A = [x + 1 for x in range(N)]
    random.seed(time.time())
    random.shuffle(A)

# This step is activating the chosen sorting method.
    if method == "b":
        title = "Bubble sort"
        generator = bubblesort(A)
    elif method == "i":
        title = "Insertion sort"
        generator = insertionsort(A)
    elif method == "m":
        title = "Merge sort"
        generator = mergesort(A, 0, N - 1)
    elif method == "q":
        title = "Quicksort"
        generator = quicksort(A, 0, N - 1)

# This step is to initialize the figure and title
    fig, ax = plt.subplots()
    ax.set_title(title)
    bar_rects = ax.bar(range(len(A)), A, align="edge")
    ax.set_xlim(0, N)
    ax.set_ylim(0, int(1.07 * N))

# This is a count machine to count the amount of exchange times.
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    iteration = [0]

# This step is to let the figure move like animation.
    def update_fig(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("operation times count: {}".format(iteration[0]))

# This step is calling the Matplotlib animation function.
# The usage instruction can be found on https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation
    anim = animation.FuncAnimation(fig, func=update_fig,
                                   fargs=(bar_rects, iteration), frames=generator, interval=2,
                                   repeat=False)
    plt.show()
