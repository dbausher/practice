/*http://practice.geeksforgeeks.org/problems/compare-two-linked-lists/1*/


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
      if(node1 != null && node2 != null){
        if(node1.data == node2.data){
          return compare(node1.next, node2.next);
        }else{
          return node1.data>node2.data?1:-1;
        }
      }
      if(node1 == null && node2 == null){
        return 0;
      }

      return node1==null?-1:1;

    }
}