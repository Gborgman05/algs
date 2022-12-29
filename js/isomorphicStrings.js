/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    var convert = function(st, start, char) {
        n = ""
        for(let j = 0; j<st.length; j++) {
            if(st[j] == start) n += char;
            else {
                n += st[j]
            }
        }
        console.log(start, char)
        console.log(n)
        return n;
    }
    if(s.length != t.length) return false;
    seen = [];
    for (let i = 0; i<t.length;i++) {
        if (s[i] != t[i]) {
            
            if (!(s[i] in seen || t[i] in seen)){
                console.log(seen)
                console.log(s[i], t[i])
                seen.push(s[i])
                seen.push(t[i])
                s = convert(s, s[i], t[i])
            }
            else {
                return false
            }
        }
        else {
            seen.push(s[i])
            // seen.push(t[i])
        } 
    }
    // console.log(s)
    return s == t
};