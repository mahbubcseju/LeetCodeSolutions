/**
 * @param {character[][]} matrix
 * @return {number}
 */
var maximalRectangle = function(matrix) {
    let rowSize = matrix.length;
    if (rowSize === 0) {
        return 0;
    }
    let columnSize = matrix[0].length;
    let result = 0;
    for(let i = 0; i < rowSize; i++) {
        let musk = new Array(columnSize).fill(1);
        for(let j = i; j < rowSize; j++){
            for(let k = 0; k < columnSize; k++){
                musk[k] &= matrix[j][k];
            }
            let cnt = 0;
            for(let k = 0; k < columnSize; k++){
                cnt = ((k == 0 || musk[k] == 0)? musk[k]: musk[k] + cnt);
                result = Math.max(cnt * (j-i+1), result);
            }
        }
    }
    return result;
};