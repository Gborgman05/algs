/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    var subroutine = function(start, end) {
        if(start > end) {
            return -1
        }
        let pivot = Math.floor((start + end) / 2)
        if(nums[pivot] > target) {
            return subroutine(start, pivot - 1)
        }
        if(nums[pivot] < target) {
            return subroutine(pivot + 1, end)
        }
        else {
            return pivot
        }
    }
    return subroutine(0, nums.length - 1)
    
};