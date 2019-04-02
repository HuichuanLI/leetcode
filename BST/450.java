// true answer 
public class Solution {
    public TreeNode deleteNode(TreeNode root, int key) {
        if(root == null) return root;
        
        if(key == root.val) {
            if(root.left == null) return root.right;
            else if(root.right == null) return root.left;
            
            TreeNode deleted = root;
            root = min(root.right);
            root.right = deleteMinHelper(deleted.right);
            root.left = deleted.left;
        } else if(key < root.val) {
            root.left = deleteNode(root.left, key);
        } else {
            root.right = deleteNode(root.right, key);
        }
        return root;
    }
    
    private TreeNode min(TreeNode root) {
        while(root.left != null) root = root.left;    
        return root;
    }
    
    private TreeNode deleteMinHelper(TreeNode curr) {
        if(curr.left == null) return curr.right;
        curr.left = deleteMinHelper(curr.left);
        return curr;
    }
}

// my answer
class Solution {
    private TreeNode getMin(TreeNode node){
        while(node.left != null) node = node.left;    
        return node;
    }
    
    private TreeNode removeMin(TreeNode node) {
        if (node.left == null) {
            return node.right;
        }
        node.left = removeMin(node.left);
        return node;
    }
    public TreeNode deleteNode(TreeNode node, int key){
        if(node == null){
            return null;
        }
        if(node.val == key){
            if(root.left == null) return root.right;
            else if(root.right == null) return root.left;
            
            TreeNode cur = node;
            TreeNode node = min(cur.right);
            node.right = removeMin(cur.right);
            node.left = cur.left;
            return cur;
        }else if(node.val > key){
                node.left = deleteNode(node.left,key);
            }else{
                node.right = deleteNode(node.right,key);
                
            }
    
        return node;
        
    }
}
