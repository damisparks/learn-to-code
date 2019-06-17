/**
*   Return the second largest number in the array.
*   @param {Number[]} nums - An array of numbers.
*   @return {Number} The second largest number in the array.
**/
function getSecondLargest(user_input) {
    let biggest, second_biggest;
    // check if the user input is a integer!
    if (Number.isInteger(user_input)) {
        return Math.max(user_input);
    } else {
        // if the input of the user is not an integer.
        if (!Number.isInteger(user_input)) {
            biggest = user_input[0];
            second_biggest = user_input[0];
            for (var i = 0; i < user_input.length; i++) {
                if (user_input[i] > biggest) {
                    second_biggest = biggest;
                    biggest = user_input[i];
                    continue;
                }

                if ((user_input[i] > second_biggest) && (user_input[i] < biggest)) {
                    second_biggest = user_input[i];
                }
            }
            return second_biggest;
        }
    }
};

// call the function below. 
getSecondLargest([55, 44, 65, 65]);