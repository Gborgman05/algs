/**
 * @param {number[]} cost
 * @return {number}
 */
var minCostClimbingStairs = function(cost) {
    minCosts = [0, 0]
    while(minCosts.length < cost.length + 1) {
        minCosts.push(Math.min(minCosts[minCosts.length - 1] + cost[minCosts.length - 1], 
                               minCosts[minCosts.length - 2] + cost[minCosts.length - 2]))
    }    
    return minCosts[minCosts.length-1]

};