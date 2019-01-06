/* Placing 0 */
document.getElementById('btn0').addEventListener('click' ,function(){
    document.getElementById('res').insertAdjacentHTML('beforeend', '0');
});

/* Placing 1 */
document.getElementById('btn1').addEventListener('click' ,function(){
    document.getElementById('res').insertAdjacentHTML('beforeend', '1');
});

/* Clear operation */
document.getElementById('btnClr').onclick = function()
{
    (document.getElementById('res').innerHTML) = "";
};

/* Targeting the event */
function operator (input){
    var activation = input.target;
    document.getElementById('res').insertAdjacentHTML('beforeend', activation.innerHTML);
}

/** Calling the event */
document.getElementById('btnSum').onclick = operator;
document.getElementById('btnMul').onclick = operator;
document.getElementById('btnDiv').onclick = operator;
document.getElementById('btnSub').onclick = operator;

/** To be continued. */