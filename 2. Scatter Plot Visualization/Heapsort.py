#
# Created by Jiang Long for CS301 DKU Fall 2021
#

import random, functools, visualization


#-------------------------------------------------
# Note: The implementation should follow textbook closely
#-------------------------------------------------

def PARENT(i): 
    # Complete the code here, see README on course website for problem description and instructions.
    return (i - 1)//2




def LEFT(i):  
    # Complete the code here, see README on course website for problem description and instructions.
    return 2*i +1




def RIGHT(i):  
    # Complete the code here, see README on course website for problem description and instructions.
    return 2*i +2







# MAX_HEAP inherit from build-in class list
class MAX_HEAP:
    # constructor
    def __init__(self, A=[], key = None, verbosity = False):
        self.A = A
        self.verbosity = verbosity # debug printing
        
        self.key = key
        if self.key is None : self.key = lambda i: i
        self.heapsize = len(A)
        self.recur_depth = 0
        
        
        pass
    def HEAPSIZE(self): return self.heapsize
    def BUILD_MAX_HEAP(self, display_grid):
        
        # Complete the code here, see README on course website for problem description and instructions.
        for i in range(PARENT(self.heapsize - 1), -1, -1):
            self.MAX_HEAPIFY(i, display_grid)



        assert self.Check_IsHEAP()
        pass
    
    def Check_IsHEAP(self):
        # Complete the code here, see README on course website for problem description and instructions.
        r = True
        for i in range(1, self.heapsize):
            r =  self.A[i] <= self.A[PARENT(i)]
            if not r: break



        return r
    
    
    def MAX_HEAPIFY(self, i, display_grid):   # use self.heapsize as the heapsize
        
        self.recur_depth +=1

        # move the larger ones to the leaf
        
        # remember the current tree 
        # for use in print the tree/heap transformation

        # Coding Task
        #
        # 1. Implement MAX_HEAPIFY as in textbook
        #
        # 2. Use self.DrawTree and rIO.concat_text_block to visualize
        # the process (see README)
        #
        
        # Complete the code here, see README on course website for problem description and instructions.
        l = LEFT(i)
        r = RIGHT(i)
        if l <= self.heapsize - 1 and self.A[l] > self.A[i]:
            largest = l
        else: largest = i
        if r <= self.heapsize - 1 and self.A[r] > self.A[largest]:
            largest = r
        if not largest == i:
            visualization.display(A, display_grid, [largest, i])
            x = self.A[largest]
            self.A[largest] = self.A[i]
            self.A[i] = x             
            self.MAX_HEAPIFY(largest, display_grid)
            visualization.display(A, display_grid, [largest, i])
        self.recur_depth -= 1       
        pass
    
    def HEAP_SORT(self, display_grid):
        # Complete the code here, see README on course website for problem description and instructions.
        self.BUILD_MAX_HEAP(display_grid)
        for i in range(len(self.A) - 1, 0, -1):
            visualization.display(A, display_grid, [0, i])
            x = self.A[0]
            self.A[0] = self.A[i]
            self.A[i] = x
            visualization.display(A, display_grid, [0, i])
            self.heapsize -= 1
            self.MAX_HEAPIFY(0, display_grid)
        pass

A = visualization.list_generation(50)


display_grid = visualization.make_display_grid(50,50)

B = MAX_HEAP(A)

B.HEAP_SORT(display_grid)