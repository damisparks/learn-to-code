/*
 * Modify and return the array so that all even elements are doubled and all odd elements are tripled.
 * 
 * Parameter(s):
 * nums: An array of numbers.
 */
function modifyArray(nums) {
    let calculated, calculation, modified_array;
    calculation = function (n) {
        // using itenary operator. 
        calculated = (n % 2 == 0) ? n * 2 : n * 3;
        return calculated;
    }
    // map the array to the calculation. 
    modified_array = nums.map(calculation);
    return modified_array;
}