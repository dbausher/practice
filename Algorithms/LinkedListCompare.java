/*
Please note that it's Function problem i.e.
you need to write your solution in the form Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.*/


/*  Structure of Node
class Node
 {
    char data;
    Node next;
 
    // Constructor to create a new node
    Node(char d) 
    {
       data = d;
       next = null;
    }
 }*/
class GfG
{
    int compare(Node node1, Node node2)
    {
      Node currNode1 = node1;
      Node currNode2 = node2;
      while(currNode1 != null && currNode2 != null){
        if(Character.compare(currNode1.data,currNode2.data) == 0){
          currNode1 = currNode1.next;
          currNode2 = currNode2.next;
        }
        else{
          return Character.compare(currNode1.data,currNode2.data) < 0? -1:1;
        }
      }
      if(currNode1 == null && currNode2 == null){
        return 0;
      }

      return currNode1==null?-1:1;

    }
}