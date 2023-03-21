function zeroFilledSubarray(nums: number[]): number {
    var count_behind = 0;
    var count = 0;
    for(let i = 0; i<nums.length;i++) {
        if(nums[i] == 0) {
            count_behind += 1;
            count += count_behind;
        }
        else {
            count_behind = 0;
        }

    }
    return count
};