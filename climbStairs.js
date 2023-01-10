/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    let arr = [0, 1, 2]
    while(arr.length - 1 < n) {
        arr.push(arr[arr.length-1] + arr[arr.length-2])
    }
    return arr[n]

};