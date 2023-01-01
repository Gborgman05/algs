/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    final = new ListNode();
    saved = final
    // cur = -100
    while(list1 && list2) {
        if(list1.val <= list2.val) {
            tmp = new ListNode(list1.val)
            list1=list1.next
        }
        else {
            tmp = new ListNode(list2.val)
            list2=list2.next
        }
        final.next = tmp
        final = final.next
    }
    while(list1) {
        final.next = new ListNode(list1.val)
        list1 = list1.next
        final = final.next
    }
    while(list2) {
        final.next = new ListNode(list2.val)
        list2 = list2.next
        final = final.next
    }
    return saved.next
};