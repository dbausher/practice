'''http://practice.geeksforgeeks.org/problems/check-if-subtree/1'''


'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should print the left view of the binary tree
# Note: You aren't required to print a new line after every test case

def stringTreePre(root):
    s = ""
    s += str(root.data) + " "
    if(root.left):
        s += stringTreePre(root.left)
    if(root.right):
        s += stringTreePre(root.right)
    return s

def stringTreeIn(root):
    s = ""
    if(root.left):
        s += stringTreeIn(root.left)
    s += str(root.data) + " "
    if(root.right):
        s += stringTreeIn(root.right)
    return s

def stringTreePost(root):
    s = ""
    if(root.left):
        s += stringTreePost(root.left)
    if(root.right):
        s += stringTreePost(root.right)
    s += str(root.data) + " "
    return s

def isSubTree(T1, T2):
    T1strPre = stringTreePre(T1)
    T2strPre = stringTreePre(T2)
    T1strIn = stringTreeIn(T1)
    T2strIn = stringTreeIn(T2)
    T1strPost = stringTreePost(T1)
    T2strPost = stringTreePost(T2)
    if(T2strPre in T1strPre and T2strIn in T1strIn and T2strPost in T1strPost):
        return 1
    return 0
