function isPalindrome(s: string): boolean {
    let a: number = 0;
    s = s.replace(/[^A-Z0-9]+/gi, "").toUpperCase();
    let b: number = s.length - 1;
    while(a < b) {      
        if(s[a] != s[b]) return false;
        a++;
        b--;
    }
    return true
};