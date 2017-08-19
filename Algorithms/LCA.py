'''http://practice.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-bst/1'''


# Your task is to complete this function
# function should return the required lca node
import collections
def LCA(root, a, b):
    q = collections.deque()
    q.appendleft(root)
    while(len(q) > 0):
        curr = q.pop()
        if((curr.data <= a and curr.data >= b) or (curr.data >= a and curr.data <= b)):
            return curr
        if(curr.right):
            q.appendleft(curr.right)
        if(curr.left):
            q.appendleft(curr.left)