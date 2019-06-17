const btns = Array.from(document.getElementsByTagName('button'));
const rotating_number = [4,1,2,7,5,3,8,9,6];
let empty_array = new Array(9);
document.getElementById('btn5').onclick = function() {
    btns.forEach((current, index) => empty_array[index] = current.innerHTML);
    btns.forEach((current, index) => current.innerHTML = empty_array[rotating_number[index] - 1]);
};
