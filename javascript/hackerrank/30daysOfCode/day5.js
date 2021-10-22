/**
 * this was my solution : 
 * Day 5: Loops
 */

function main() {
    const n = parseInt(readLine().trim(), 10);
    
    const maxCount = 10
    for(let i = 1; i <= maxCount; i++) {
        const result = parseInt(n*i)
        console.log(`${n} x ${i} = ${result}`)
    }
}
