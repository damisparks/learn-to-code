function main() {
    const N = parseInt(readLine().trim(), 10);
    
    
    if(N >= 1 && N <= 100) {
        const is_odd = (N % 2 > 0) 
        
        if(is_odd){
            console.log('Weird')
        }
        if(N % 2 === 0 && N >= 2 && N <= 5) {
            console.log('Not Weird') 
        }
        if(N % 2 === 0 &&  N >= 6 && N <= 20){
            console.log('Weird')
        }
        if(N % 2 === 0 && N > 20 ){
            console.log('Not Weird')
        }      
    }
}