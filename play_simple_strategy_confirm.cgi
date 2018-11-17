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

print<<EOP;

<!DOCTYPE html>
<html>
<head><title>Rock paper scissor</title>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

</head>
<body>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="#">Rock Paper Scissors</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <a class="nav-link" href="index.cgi">Main Page<span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item active">
          <a class="nav-link" href="instructions.cgi">Instructions<span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item active">
          <a class="nav-link" href="create_strategy.cgi">Create Strategy<span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item active">
          <a class="nav-link" href="beat_strategy.cgi">Beat Strategy<span class="sr-only">(current)</span></a>
        </li>
      </ul>

      <ul class="navbar-nav ml-auto">
        <li class="nav-item active">
          <a class="nav-link" href="logout.cgi">Logout <span class="sr-only">(current)</span></a>
        </li>
      </ul>
    </div>
  </nav>


<div class="container" style="padding:20px">
      <div class="jumbotron">
         <h1 class="display-4">Play simple strategy results</h1>
         <p class="lead">here you see how you did vs strategy</p>


EOP

$s_name = param("s_name");
print "<p class='lead'>strategy name: $s_name</p>";

print<<EOP;

         <hr class="my-4">
      </div>


EOP






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



print("total points : $total_points (maximum is 10)");
print("</div>");

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
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

</head>
<body>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="#">Rock Paper Scissors</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <a class="nav-link" href="index.cgi">Main Page<span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item active">
          <a class="nav-link" href="instructions.cgi">Instructions<span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item active">
          <a class="nav-link" href="create_strategy.cgi">Create Strategy<span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item active">
          <a class="nav-link" href="beat_strategy.cgi">Beat Strategy<span class="sr-only">(current)</span></a>
        </li>
      </ul>

      <ul class="navbar-nav ml-auto">
        <li class="nav-item active">
          <a class="nav-link" href="login_intro.cgi">Sign in <span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item active">
          <a class="nav-link" href="register_intro.cgi">Sign up <span class="sr-only">(current)</span></a>
        </li>
      </ul>
    </div>
  </nav>

<h1>You must be logged in to see this</h1>

</body>
</html>

EOP
}
