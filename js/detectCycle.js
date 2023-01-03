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
    seen = {}
    cnter = 0
    while(head) {
        if(head in seen) {
            return head
        }
        else {
            seen[head] = cnter
            head = head.next
        }
        cnter++;
    }
    return head    
};