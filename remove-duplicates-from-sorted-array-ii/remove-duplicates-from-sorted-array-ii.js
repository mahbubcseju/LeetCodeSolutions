/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let position = -1;
    for(let i = 0; i < nums.length; i++) {
        if (position > 0 && nums[position - 1] == nums[i]) {
            continue
        }else {
            nums[++position] = nums[i];
        }
    }
    return position + 1
};