/**
 * @param {string} secret
 * @param {string} guess
 * @return {string}
 */
var getHint = function(secret, guess) {
    counted = {}
    for(let i=0;i<secret.length;i++) {
        if(counted[secret[i]]) {
            counted[secret[i]] += 1
        }
        else {
            counted[secret[i]] =1
        }

    }
    bulls = 0
    cow = 0
    for(let i= 0;i<secret.length;i++) {
        if(secret[i] == guess[i]) {
            bulls += 1
            counted[secret[i]] -= 1
        } }

    for(let i= 0;i<secret.length;i++) {
        if(secret[i] == guess[i]) {
            1 + 1;
        }
        else if(counted[guess[i]] && counted[guess[i]] > 0) {
            cow += 1
            counted[guess[i]] -= 1
            
        }

    }
    return `${bulls}A${cow}B`
    
};