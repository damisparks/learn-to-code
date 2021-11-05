/**
 * 
 * Day 6: Let's Review
 */


function getStringValue(element) {
    return element.reduce((rev, char)=> `${rev}${char}`, '')
}


function setIndexation(item) {
    const L = item[0] - 1
    const S = item.slice(1)

    S.forEach((x, y) => {
        const isEvenIndex = []
        const isOddIndex = []
        for (let i = 0; i < x.length; i++) {
            if(i%2 === 0) {
                isEvenIndex.push(x[i])
            }
            if(i%2 > 0){
                isOddIndex.push(x[i])
            }
        }
        console.log(`${getStringValue(isEvenIndex)} ${getStringValue(isOddIndex)}`)
    })
}

function processData(input) {
    const getValue = input.split('\n');
    setIndexation(getValue)
} 

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});
