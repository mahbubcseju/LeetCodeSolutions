/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let result = 0;
    for(let el in nums){
        result ^= nums[el];
    }
    return result;
};