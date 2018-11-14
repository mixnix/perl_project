#!/usr/bin/perl -w

use CGI qw(:standard -debug);
use CGI::Carp qw(fatalsToBrowser);

use utf8;
use Encode;

sub calculate_move{
  my($op_mov, $player_move) = @_;
  if($op_mov eq $player_move){
    return 0.5;
  }elsif(($op_mov eq "r" && $player_move eq "s") || 
  ($op_mov eq "p" && $player_move eq "r") ||
  ($op_mov eq "s" && $player_move eq "p")){
    return 0;
  }elsif(($op_mov eq "s" && $player_move eq "r") || 
  ($op_mov eq "r" && $player_move eq "p") ||
  ($op_mov eq "p" && $player_move eq "s")){
    return 1;
  }else{
    return 100;
  }

}

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
print "<h1>here you see how you did vs strategy</h1><br>";
$s_name = param("s_name");
print "<p>strategy name: $s_name</p>";


#loads all parameters
#name, move1
$strategy_name = param("s_name");
$move1= param("move1");
$move2= param("move2");
$move3= param("move3");
$move4= param("move4");
$move5= param("move5");
$move6= param("move6");
$move7= param("move7");
$move8= param("move8");
$move9= param("move9");
$move10= param("move10");

#print them to check value for debugiing

#open file with strategies and loads all line
$strategies_file = "simple_strategies.txt";

open(INS, "$strategies_file") || die "cant read $strategies_file";
@lines=<INS>;
close INS;

my $m1, $m2, $m3, $m4, $m5, $m6, $m7, $m8, $m9, $m10;
foreach $line(@lines){
  if(index($line, $strategy_name) != -1){
	chomp $line;
    ($niepotrzebne, $m1, $m2, $m3, $m4, $m5, $m6, $m7, $m8, $m9, $m10)=split / /,$line,11;
  }
}
$total_points = 0;
$total_points += calculate_move($m1, $move1);
$total_points += calculate_move($m2, $move2);
$total_points += calculate_move($m3, $move3);
$total_points += calculate_move($m4, $move4);
$total_points += calculate_move($m5, $move5);
$total_points += calculate_move($m6, $move6);
$total_points += calculate_move($m7, $move7);
$total_points += calculate_move($m8, $move8);
$total_points += calculate_move($m9, $move9);
$total_points += calculate_move($m10, $move10);
print("total points : $total_points");

#for through all lines and check for containing of straegy name
#when you find good line then use split to split it into 10 different arugments

#show form with 10 radio buttons that you have to pick move and then submit
#create new page that shows you your score, there you will load strategy and check which round were win. 1 point for win 0.5 point for draw and 0 points for losing round

#from there you can only go back
#that shall be enough for today
#after taht spend one day on implementing bootstrap and check how it looks
#show it to professor on monday

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
