/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let last = 0
    let flag = 0
    for (let i=0;i< s.length;i++) {
        if (s[i] != " ") {
            if (flag == 1){
                flag = 0
                last = 0
            }
            last += 1
        }
        else {
            flag = 1
        }

    }
    return last
    
};