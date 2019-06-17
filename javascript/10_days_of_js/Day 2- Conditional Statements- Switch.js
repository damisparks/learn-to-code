function getLetter(s) {
    let letter;
    // using switch 
    switch (s[0]){
            case ( 'a' || 'e' || 'o' || 'i' || u):
                letter = 'A';
                break;
                
            case ('b' || 'c' || 'd' || 'f' || 'g'):
                letter = 'B';
                break;
                
            case ('h' || 'j' || 'k' || 'l' || 'm'):
                letter = 'C';
                break;
                
            case ('z' || 'n' || 'p' || 'q' || 'r' || 's' || 't' || 'v' || 'w' || 'x' || 'y' ):
                letter = 'D';
                
        
        /* this is an alternate way to it as well. 
        case "a":
        case "e":
        case "i":
        case "o":
        case "u":
            letter = "A";
            break;
        case "b":
        case "c":
        case "d":
        case "f":
        case "g":
            letter = "B";
            break;
        case "h":
        case "j":
        case "k":
        case "l":
        case "m":
            letter = "C";
            break;        
        default:
            letter = "D";*/
    }
    return letter;
}