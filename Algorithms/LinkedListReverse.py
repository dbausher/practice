'''http://practice.geeksforgeeks.org/problems/reverse-a-linked-list-in-groups-of-given-size/1'''


"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
  This is method only submission.
  You only need to complete the method.
"""
def reverse(head, k):
    nodes = list()
    while(head):
        nodes.append(head)
        head = head.next

    reversedBoys = []

    while(nodes):
        for i in reversed(range(k)):
            if(i < len(nodes)):
                reversedBoys.append(nodes.pop(i))

    newHead = reversedBoys[0]
    curr = newHead
    for node in reversedBoys:
        curr.next = node
        curr = node
    curr.next = None
    return newHead



