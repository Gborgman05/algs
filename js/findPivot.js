/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
    let lsum = 0;
    let rsum =nums.reduce((a, b) => a + b, 0)
    console.log(rsum)
    for(let i = 0; i<nums.length;i++) {
        rsum -= nums[i]
        if (lsum == rsum) return i;
        else {
            lsum += nums[i]
            
        }

    }
    return -1
};