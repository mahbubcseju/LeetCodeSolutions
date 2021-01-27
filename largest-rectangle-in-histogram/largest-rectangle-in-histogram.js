/**
 * @param {number[]} heights
 * @return {number}
 */
var largestRectangleArea = function(heights) {
    let leftStack = [];
    let result = new Array(heights.length).fill(0);
    for(let i = 0; i < heights.length; i++) {
        while(leftStack.length && heights[leftStack[leftStack.length - 1]] >= heights[i]) {
            leftStack.pop();
        }
        let leftMost = ((leftStack.length > 0)? leftStack[leftStack.length - 1] : -1);     
        result[i] = i - leftMost - 1;
        leftStack.push(i);
    }
    while(leftStack.length > 0){
        leftStack.pop();
    }
    let ans = 0;
    for(let i = heights.length - 1; i >= 0; i--){
        while(leftStack.length && heights[leftStack[leftStack.length - 1]] >= heights[i]) {
            leftStack.pop();
        }
        let rightMost = (leftStack.length > 0? leftStack[leftStack.length - 1] : heights.length);
        result[i] += rightMost - i;
        ans = Math.max(ans, heights[i] * result[i]);
        leftStack.push(i);
    }
    return ans;
};