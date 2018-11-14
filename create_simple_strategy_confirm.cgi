#!/usr/bin/perl -w

use CGI qw(:standard -debug);
use CGI::Carp qw(fatalsToBrowser);

use utf8;
use Encode;

#firstly check if the guy is logged in, if he is then we dont do anything beside saying
#him that he is logged in and showing button to go back to main page

#load all cookie data to check if his  cookie is the right one
$cookie_file = "cookie.txt";
open(IN, "$cookie_file") || die "cant read $cookie_file";
@lines=<IN>;
close IN;
chomp @lines;

#print "@lines";
foreach $line(@lines){
   ($id, $id_number)=split / /,$line,2;
   $cookie_hash{$id}=$id_number;
}

$cookie= cookie('random-name');
($num_from_cookie, $id_from_cookie)=split / /,$cookie;
if ($cookie && $cookie_hash{$id_from_cookie} && ($cookie_hash{$id_from_cookie}==$num_from_cookie)){

print header();
print start_html();
print "you are already logged in";
print "<br>";
print "<a href='index.cgi'>main page</a><br>";
print "<a href='logout.cgi'>logout</a><br>";
print "<a href='instructions.cgi'>instructions</a><br>";
print "<a href='create_strategy.cgi'>create strategy</a><br>";
print "<a href='beat_strategy.cgi'>beat strategy</a><br>";
print "<h1>create simple strategy confirmation</h1><br>";
print "<p>new simple strategy created</p>";

#loads all parameters
#name, move1
$strategy_name = param("name");
$move1= param("move1");
$move2= param("move2");
$move3= param("move3");
$move4= param("move4");
$move5= param("move5");
$move6= param("move6");
$move7= param("move7");
$move8= param("move8");
$move9= param("move9");
$move10=param("move10");

#10 moves
#print them to check value for debugiing
$line_to_file = $strategy_name . " " . $move1 . " " . $move2 . " " . $move3 . " " . $move4 . " " . $move5 . " " . $move6 . " " . $move7 . " " . $move8 . " " . $move9 . " " . $move10 . "\n";
#opens file that is gonna hold name at beginning of line and all lines

$strategies_file = "simple_strategies.txt";
open(STROUT, ">>$strategies_file") || die "cant open for appending $strategies_file";
print STROUT "$line_to_file";
close STROUT



#pushes all parameters to one string variable, adds end of line character and appends to file

#after writing this code for 1 move check manually if it works, after writing for 10 moves also check if it works
#check it 2 times to check if new line character works



}else{


print<<EOP;

<!DOCTYPE html>
<html>
<head><title>Rock paper scissor</title>
</head>
<body>

<h3>Here you can play rock paper scissor</h3>
<form action="register_intro.cgi">
<input type="submit" value="Sign Up">
</form>
<form action="login_intro.cgi">
<input type="submit" value="Sign In">
</form>

<form action="game.cgi" method="post">

<!--br>
Select your move:<br>
<input type="radio" name="move" value="rock" checked="true"> rock </input><br>
<input type="radio" name="move" value="paper"> paper </input><br>
<input type="radio" name="move" value="scissors"> scissor </input><br>

<input type="submit" value="Lets fight">

</form>

-->
</body>
</html>

EOP
}
