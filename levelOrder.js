// INCOMPLETE, IMPLEMENTED INCORRECT TRAVERSAL
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function(root) {
    if(root) {

        let a = levelOrder(root.left).concat([root.val]).concat(levelOrder(root.right))
        console.log(a)
        return a
    }
    console.log(root)

    return []
    
};