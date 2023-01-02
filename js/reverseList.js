/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    first = true
    ptr = null
    while(head) {
        if (first) {
            ptr = new ListNode(head.val)
            first = false
        }
        else{
            tmp = new ListNode(head.val, ptr)
            ptr = tmp
        }
        head = head.next

    }
    return ptr
};