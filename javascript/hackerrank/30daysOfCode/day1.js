/**
 * this was my solution : 
 * Day 1: Data Types
 */
function main() {
    var i = 4
    var d = 4.0
    var s = "HackerRank "
    // Declare second integer, double, and String variables.
    let isInt;
    let isFloat;
    let isString; 

    // Read and save an integer, double, and String to your variables.
    isInt = +(readLine());
    isFloat = +(readLine());
    isString = readLine();
    // Print the sum of both integer variables on a new line.
    console.log(i + isInt);
    // Print the sum of the double variables on a new line.
    console.log((d + isFloat).toFixed(1))

    // Concatenate and print the String variables on a new line
    // The 's' variable above should be printed first.
    console.log(s + isString);

}