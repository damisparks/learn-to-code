/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {

    // define variable vowel
    let vowel; 
    vowel = ['a', 'e', 'i', 'o', 'u']; // create an array of vowels 
    for (var a = 0; a < s.length; a++) {
        // check if index is > -1 (if not found), greater if found. 
        if (vowel.indexOf(s[a]) > -1) {
            console.log(s[a]);
        }
    }
    for (var b = 0; b < s.length; b++){
        // check index is less than 0, if found it will be greater than 0
        if (vowel.indexOf(s[b]) < 0 ) { 
            console.log(s[b]);
        }
    }
}


