'''http://practice.geeksforgeeks.org/problems/merge-list-alternatingly/1'''


# your task is to complete this function
# function should return a list of the
# two new heads
def mergeList(head1, head2):
    curr = head1
    while(curr and head2 and curr.next):
        nextBoy = curr.next
        nextHead = head2.next
        head2.next = curr.next
        curr.next = head2
        head2 = nextHead
        curr = nextBoy
        
    if(head2):
        curr.next = head2
        head2 = head2.next
        curr.next.next = None
        

    return [head1, head2]