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
         <h1 class="display-4">Create simple strategy confirmation</h1>
         <p class="lead">new simple strategy created</p>
         <hr class="my-4">
      </div>
</div>

EOP



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