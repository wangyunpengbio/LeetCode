class Solution {
    //后序遍历，基本思路和前序遍历一样，入栈顺序为根、右、左，出栈时判断是否第二次入栈节点，是则输出该节点
    public List<Integer> postorderTraversal(TreeNode root) {
        Set<TreeNode> set = new HashSet<>();
        if(root == null)
            return new ArrayList<>();
        List<Integer> res = new LinkedList<>();
        Deque<TreeNode> stack = new LinkedList<>();
        stack.push(root);
        while(!stack.isEmpty()){
            TreeNode node = stack.pop();
            //如果node是第二次入栈，或者是叶子节点，直接返回node.val
            if(set.contains(node) || (node.left == null && node.right == null)){
                res.add(node.val);
            }else{
                //将根节点第二次入栈，然后依次将右节点、左节点入栈
                stack.push(node);
                if(node.right != null){
                    stack.push(node.right);
                }
                if(node.left != null){
                    stack.push(node.left);
                }
                //记录第二次入栈的节点
                set.add(node);
            }
        }
        return res;
    }
}