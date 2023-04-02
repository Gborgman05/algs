/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    // while(i <nums.length) {
    //     if (nums[i] == val) {
    //         delete nums[i]
    //     }
    //     else {
    //         i += 1
    //     }
    // }
    nums = nums.filter(i => i != val)
    return nums
    // return nums
};