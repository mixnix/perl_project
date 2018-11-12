#!/usr/bin/perl  -w

#---------------------------------------------
# Name: Rock Paper Scissors
#---------------------------------------------
# CGI input:
#   move = rock | paper | scissors (radio)
#---------------------------------------------

use CGI qw(:standard -debug);
use CGI::Carp qw(fatalsToBrowser);

$move = param("move");

#0 - rock <> 1 - paper <> 2 - scissors
$computer_move = int(rand(3));
$comp_move_string = "";
if ($computer_move == 0){
  $comp_move_string = "rock";
}elsif($computer_move == 1){
  $comp_move_string = "paper";
}elsif($computer_move == 2){
  $comp_move_string = "scissors";
}

$html_string = "";

if ( (($move eq "rock") && ($comp_move_string eq "scissors")) || (($move eq "paper") && ($comp_move_string eq "rock")) || (($move eq "scissors") && ($comp_move_string eq "paper")) ){
   $html_string = "You win";
}elsif( (($move eq "scissors") && ($comp_move_string eq "rock")) || (($move eq "rock") && ($comp_move_string eq "paper")) || (($move eq "paper") && ($comp_move_string eq "scissors")) ){
   $html_string = "You lose";
}elsif( (($move eq "scissors") && ($comp_move_string eq "scissors")) || (($move eq "rock") && ($comp_move_string eq "rock")) || (($move eq "paper") && ($comp_move_string eq "paper")) ){
   $html_string = "It's a draw";
 }

 $html_string0 = "You picked $move and computer picked $comp_move_string.";

#-------------
# print HTML

print header();

print<<EOP; 

<head><title>Rock paper scissors game</title></head>
<body>
<hr><h1>Rock paper scissors game</h1><hr>
$html_string0 $html_string
<p>

EOP


print<<EOP;

<hr>

<input type="button" value="Back to Form" onClick="history.back()">
</body>
</html>

EOP
