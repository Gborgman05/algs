/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var detectCycle = function(head) {
    while(head) {
        if(head.visited) {
            delete head.visited
            return head
        }
        else {
            head.visited = true
            head = head.next
            
        }
        // cnter++;
    }
    return null
};