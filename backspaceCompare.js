/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var backspaceCompare = function(s, t) {
    let first = []
    let second = []
    for(char in s) {
        if(s[char] == "#") {
            first.pop()
        }
        else{
            first.push(s[char])
        }
    }
    for(char in t) {
        if(t[char] == "#") {
            second.pop()
        }
        else{
            second.push(t[char])
        }
    }
    console.log(first, second)
    if(first.length != second.length) return false;
    for (var i = 0; i < first.length; ++i) {
        if (first[i] !== second[i]) return false;
    }
    return true;
    
};