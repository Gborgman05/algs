/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {
    pathsTo = []
    for(let i=0;i<m;i++) {
        pathsTo.push([])
        for(let j=0;j<n;j++){
            if(i==0) {
                pathsTo[i].push(1)
            }
            else if(j==0) {
                pathsTo[i].push(pathsTo[i-1][j])

            }
            else {
                pathsTo[i].push(pathsTo[i-1][j] + pathsTo[i][j-1])
            }
        }
    }
    return pathsTo[m-1][n-1]
};