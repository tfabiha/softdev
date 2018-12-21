//ENDGAME
//T Fabiha, Michelle Tang
//SoftDev1 pd6
//K30
//2018-12-20

var changeHeading = function(e) {
    var h = document.getElementById("h");
    h.innerHTML = this.innerHTML;
    console.log("changeHeading");
};

var changeHeadingBack = function(e) {
    var h = document.getElementById("h");
    h.innerHTML = "Hello World!";
};

var removeItem = function(e){
    this.remove();
};

var lis = document.getElementsByTagName("li");

for (var i =0; i < lis.length; i ++){
    lis[i].addEventListener('mouseover', changeHeading);
    lis[i].addEventListener('mouseout', changeHeadingBack);
    lis[i].addEventListener('click', removeItem);
};

var addItem = function(e){
    var list = document.getElementById("thelist");
    var item = document.createElement("li");
    item.innerHTML = "WORD";
    item.addEventListener('mouseover', changeHeading);
    item.addEventListener('mouseout', changeHeadingBack);
    item.addEventListener('click', removeItem);
    list.appendChild( item );
};

var button = document.getElementById("b");
button.addEventListener( 'click', addItem );

var f1 = 0;
var f2 = 1;

var addFib = function(e)
{
    var list = document.getElementById("fiblist");
    var item = document.createElement("li");
    
    item.innerHTML = f1;
    list.appendChild( item );
    console.log("addFib");

    var x = f1 + f2;
    f1 = f2;
    f2 = x;

};

var fb = document.getElementById("fb");
fb.addEventListener("click", addFib);
