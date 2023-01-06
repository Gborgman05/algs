/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function(s) {
    let letters = {};
    let count = 0;
    let odds = 0;
    for(let i = 0; i < s.length;i++) {
        if (letters[s[i]]) {
            if (letters[s[i]] == 1) {
                count += 2;
                letters[s[i]] = 0;
                odds -= 1;
            }
            else {
                letters[s[i]] = 1;
                odds += 1;
            }
        }
        else {
            letters[s[i]] = 1;
            odds += 1;
        }
    }
        if (odds>0) {
        return count + 1
    }
    else {
        return count
    }
    
};