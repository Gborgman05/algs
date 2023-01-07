/**
 * // Definition for a Node.
 * function Node(val, children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */

/**
 * @param {Node|null} root
 * @return {number[]}
 */
var preorder = function(root) {
    if (root && root.children) {
        lst = [root.val]
        for(let i= 0;i<root.children.length;i++) {
            lst = lst.concat(preorder(root.children[i]))
        }
        return lst
    }
    else {
        return []
    }
};