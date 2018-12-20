// ENDGAME - Michelle Tang, T Fabiha
// SoftDev1 pd6
// K28 -- Sequential Progression
// 2018-12-18

var fibonacci = function(n)
{
    if (n < 2)
    {
	return 1;
    }
    else
    {
	return fibonacci(n - 1) + fibonacci(n - 2);
    }
};

var gcd = function (a, b){
    current_gcd = 1;
    i = 1;
    
    while (i <= a && i <= b){
	if (a%i == 0 && b%i ==0){
	    current_gcd = i;
	}
	i++;
    }
    
    return current_gcd;
};

var list = ["taylor","swift", "austin", "romeo","dojo"];

var random_student = function(){
    var ran = list[random_num(list.length)];
    // console.log(ran);
    return ran;
};

var random_num = function(length){
    var num =  Math.floor( Math.random()*length );
    return num;
};

var test = function()
{
    return 5;
};

var fibFunc = function()
{
    var f = fibonacci(8);
    console.log(f);
    this.innerHTML = f;
};

var gcdFunc = function()
{
    var gg = gcd(12, 8);
    console.log(gg);
    this.innerHTML = gg;
};

var randStuFunc = function()
{
    var stu = random_student();
    console.log(stu);
    this.innerHTML = stu;
};
