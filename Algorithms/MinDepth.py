'''http://practice.geeksforgeeks.org/problems/minimum-depth-of-a-binary-tree/1'''


# Your task is to complete this function
# Function should return an integer
import collections
def minDepth(root):
        q = collections.deque()
        q.appendleft((root,1))
        while len(q) > 0:
            curr,depth = q.pop()
            if(curr.left):
                q.appendleft((curr.left,depth + 1))
            if(curr.right):
                q.appendleft((curr.right,depth+1))
            elif(not curr.left):
                return depth
        return -1