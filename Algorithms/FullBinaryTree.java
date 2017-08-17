/*http://practice.geeksforgeeks.org/problems/full-binary-tree/1*/


/*Complete the function below
Node is as follows:
class Node 
{
    int data;
    Node left, right;
  
    Node(int item) 
    {
        data = item;
        left = right = null;
    }
}
*/
class GfG
{
    boolean isFullTree(Node node)
    {   
        if(node.right == null && node.left == null){
            return true;
        }
        else if(node.right != null && node.left != null){
            return isFullTree(node.right) && isFullTree(node.left);
        }
        else{
            return false;
        }
    }
}