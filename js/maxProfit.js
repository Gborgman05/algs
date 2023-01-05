/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    profit = 0
    small = prices[0]
    for(let j=0;j<prices.length;j++) {
        if(prices[j] < small) {
            small = prices[j];
        }
        let prof = prices[j] - small
        if(prof> profit) { 
        profit = prof;
        }

    }
    return profit
};