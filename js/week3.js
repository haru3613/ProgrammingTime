var searchInsert = function(nums, target) {
    let i = 0;
    while(i <= nums.length){
        if (nums[i] >= target) return i;
        else if (i === nums.length) return i
        i++
    }
};