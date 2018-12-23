/*
 * Complete the reverseString function
 + Try to reverse string using the split, reverse, and join methods. 
 * Use console.log() to print to stdout.
 */
function reverseString(s) {
    try {
        s = s.split("").reverse().join("");
        console.log('this was tried!');
    } catch(e) {
        console.log(e.message);
    } finally {
        console.log(s);
    }
}