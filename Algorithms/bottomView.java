/*http://practice.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1i-03*/


/* Tree node class
class Node {
    int data; //data of the node
    int hd; //horizontal distance of the node
    Node left, right; //left and right references
    public Node(int key)
    {
        data = key;
        hd = Integer.MAX_VALUE;
        left = right = null;
    }
}*/
class GfG
{
    // Should print bottom view of tree with given root
    public void bottomView(Node root)
    {
        Map<Integer,Integer> columns = new TreeMap<>();
        Queue<Node> q = new LinkedList<Node>();
        root.hd = 0;
        q.add(root);
        while(q.peek() != null){
            Node curr = q.remove();
            columns.put(curr.hd,curr.data);
            if(curr.left != null){
                curr.left.hd = curr.hd - 1;
                q.add(curr.left);
            }
            if(curr.right != null){
                curr.right.hd = curr.hd + 1;
                q.add(curr.right);
            }

        }
        String output = "";
        for(int col:columns.keySet()){
            output += columns.get(col) + " ";
        }

        System.out.print(output);


    }
}