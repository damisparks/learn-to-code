/**
 * A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

function solution(N);

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
 */
// function solution(N);

function binaryGap(params) {
  params = params.toString(2);
  let countingZeros = [];
  let one = 1;
  let zero = 0;
  let count = 0;
  let collectedZeros = [];
  let a = 0;
  let ahead = 1;

  while (count < params.length) {
    if (params[count] == 1) {
      countingZeros.push(count);
      console.log(count);
      //let first_index = params.indexOf(params[count]);
      //let second_index = params.indexOf(params[count], count + 1)

      //console.log('Position is : ' + count + ' Found 1 :  ' + params[count] + ' Index : ' + first_index)
      //console.log('Position is : ' + count + ' Found 1 :  ' + params[count] + ' Second Index  : ' + second_index)

      let difference;
      console.log(
        "SOmething : " +
          params.slice(params[count], ahead) +
          " Param Count : " +
          count +
          " : " +
          ahead
      );
      difference = params.slice(params[count] + 1, count + 1).length;
    }

    count++;
    ahead = count + 1;
  }
  console.log(countingZeros);

  /*
  for (let i = 0; i < params.length; i++) {
    console.log(i)
    if(params[i] == 1){
      params[i++]
      let first_index = params.indexOf(i);
      //console.log(params[i] + ' : First Position is at ' + first_index)
      for (let j = 0; j < params.length; j++){
        
        let second_index = params.indexOf(i, i+1)
        //console.log('Second index : ' + params[j] + ' is ' + second_index)
        let getting_zero = params.slice(first_index+1, second_index);
        console.log(getting_zero, getting_zero.length)
        params[i++]
      }  
    }
   
      
  
  }*/

  return params;
}

sampleBinary1 = 529;
sampleBinary2 = 15;
sampleBinary3 = 32;
console.log("sampleBinary1 : " + binaryGap(sampleBinary1) + " ");
//console.log('sampleBinary2 : ' + binaryGap(sampleBinary2))
//console.log('sampleBinary3 : ' + binaryGap(sampleBinary3))
