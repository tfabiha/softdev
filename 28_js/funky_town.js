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
}

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
}

//var list = ["taylor","swift", "austin", "romeo","dojo"];

var random_student = function( list ){
  return list[random_num(list.length)];
}

var random_num = function(length){
  return Math.floor( Math.random()*length );
}

var test = function(n)
{
  return 5;
}
