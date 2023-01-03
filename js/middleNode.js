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
var middleNode = function(head) {
    ptr1 = head;
    ptr2 = head;
    flipper = false;
    while(ptr2) {
        ptr2 = ptr2.next;
        if (flipper) {
            flipper = false;
            ptr1 = ptr1.next;
        }
        else {
            flipper = true;
        }
        if(!ptr2) {
            return ptr1
        }
    }
    return ptr1
    
};