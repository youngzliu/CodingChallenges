/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public IList<string> BinaryTreePaths(TreeNode root) {
        List<string> paths = new List<string>();
        if(root != null){
            traverseTree(root, "", paths);
        }
        return paths;
    }
    
    public void traverseTree(TreeNode root, string currentPath, List<string> paths){
        if(root.left == null && root.right == null){
            paths.Add(currentPath + root.val);
        }
        else{
            if(root.left != null){
                traverseTree(root.left, currentPath + root.val + "->", paths);
            }
            if(root.right != null){
                traverseTree(root.right, currentPath + root.val + "->", paths);
            }
        }
    }
}