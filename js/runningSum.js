/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    let cur = 0
    for (let i = 0; i<nums.length; i++) {
        cur += nums[i]
        nums[i] = cur
    }
    return nums
    
};