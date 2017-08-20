/*http://practice.geeksforgeeks.org/problems/reverse-alternate-levels-of-a-perfect-binary-tree/1*/


/*
// A Binary Tree node
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
// class to access index value by reference
class Index 
{
   int index;
}
*/
class GfG
{
    Index index_obj = new Index();  // Object of class Index
        void reverseAlternate(Node node)
        {
            Map<Integer,List<Integer>> odds = new HashMap<>();
            Map<Node,Integer> depths = new HashMap<>();
            Queue<Node> q = new LinkedList<Node>();
            depths.put(node,0);
            q.add(node);
            while(q.peek() != null){
                Node curr = q.remove();
                if(depths.get(curr)%2 == 1){
                    if(odds.get(depths.get(curr)) == null){
                        odds.put(depths.get(curr), new ArrayList<>());
                    }
                    odds.get(depths.get(curr)).add(curr.data);
                }
                
                if(curr.left != null){
                    depths.put(curr.left, depths.get(curr) + 1);
                    q.add(curr.left);
                }
                if(curr.right != null){
                    depths.put(curr.right, depths.get(curr) + 1);
                    q.add(curr.right);
                }

            }

            q.add(node);
            while(q.peek() != null){
                Node curr = q.remove();
                int currDepth = depths.get(curr);
                if(curr.left != null){
                    if(currDepth%2 == 0){
                        curr.left.data = odds.get(currDepth + 1).remove(odds.get(currDepth + 1).size()-1);
                    }
                    depths.put(curr.left,currDepth + 1);
                    q.add(curr.left);
                }
                if(curr.right != null){
                    if(currDepth%2 == 0){
                        curr.right.data = odds.get(currDepth + 1).remove(odds.get(currDepth + 1).size()-1);
                    }
                    depths.put(curr.right,currDepth + 1);
                    q.add(curr.right);
                }

            }
    }
}