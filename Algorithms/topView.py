'''http://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1'''


'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should print the top view of the binary tree
# Note: You aren't required to print a new line after every test case
import collections
def printTopView(root):
    columns = {}
    out = []
    q = collections.deque()
    q.appendleft((root,0))
    while len(q) > 0:
            curr,col = q.pop()
            if col not in columns:
                columns[col] = curr.data
                out.append(curr.data)
            if(curr.left):
                q.appendleft((curr.left,col - 1))
            if(curr.right):
                q.appendleft((curr.right,col + 1))

    # for key in sorted(columns):
    #     out.append(columns[key])
    print(" ".join(list(map(str,out))), end="")
