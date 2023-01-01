/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    i = 0;
    j = 0;
    while(i < s.length && j < t.length) {
        // console.log(s[i], t[j])
        if(s[i] == t[j]) {
            i++;
            j++;
        }
        else {
            j++;
        }
    }
    // console.log(i);
    return i >=s.length;
};