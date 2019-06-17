// this increases the value of the number inside the button. 
var getButton = document.getElementById('btn');
getButton.innerHTML = 0;
getButton.onclick = function(){
    this.innerHTML++;
};
