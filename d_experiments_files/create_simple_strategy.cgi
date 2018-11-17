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
  <h1 class="display-4">Create simple strategy</h1>
  <p class="lead">Here you can create simple strategies</p>
  <hr class="my-4">
</div>
   <div class="form-check" style="padding:20px">
<form action="create_simple_strategy_confirm.cgi" method="post">

 <div class="form-group">
    <label for="Name">Example label</label>
    <input type="text" class="form-control" id="Name" name="name" placeholder="Input name">
  </div>

  <div class="row">             <!-- responsive row has 12 columns by default -->
    <div class="col-md-6">      <!-- uses 6 columns on medium and larger screens... -->
      cosik1
    </div>
    <div class="col-md-6">      <!-- uses 12 columns on smaller than medium screens -->
    cosik2
    </div>
</div>


Move 1<br>
<input type="radio" name="move1" value="r">Rock</input><br>
<input type="radio" name="move1" value="p">Paper</input><br>
<input type="radio" name="move1" value="s">Scissors</input><br>
Move 2<br>
<input type="radio" name="move2" value="r">Rock</input><br>
<input type="radio" name="move2" value="p">Paper</input><br>
<input type="radio" name="move2" value="s">Scissors</input><br>
Move 3<br>
<input type="radio" name="move3" value="r">Rock</input><br>
<input type="radio" name="move3" value="p">Paper</input><br>
<input type="radio" name="move3" value="s">Scissors</input><br>
Move 4<br>
<input type="radio" name="move4" value="r">Rock</input><br>
<input type="radio" name="move4" value="p">Paper</input><br>
<input type="radio" name="move4" value="s">Scissors</input><br>
Move 5<br>
<input type="radio" name="move5" value="r">Rock</input><br>
<input type="radio" name="move5" value="p">Paper</input><br>
<input type="radio" name="move5" value="s">Scissors</input><br>
Move 6<br>
<input type="radio" name="move6" value="r">Rock</input><br>
<input type="radio" name="move6" value="p">Paper</input><br>
<input type="radio" name="move6" value="s">Scissors</input><br>
Move 7<br>
<input type="radio" name="move7" value="r">Rock</input><br>
<input type="radio" name="move7" value="p">Paper</input><br>
<input type="radio" name="move7" value="s">Scissors</input><br>
Move 8<br>
<input type="radio" name="move8" value="r">Rock</input><br>
<input type="radio" name="move8" value="p">Paper</input><br>
<input type="radio" name="move8" value="s">Scissors</input><br>
Move 9<br>
<input type="radio" name="move9" value="r">Rock</input><br>
<input type="radio" name="move9" value="p">Paper</input><br>
<input type="radio" name="move9" value="s">Scissors</input><br>
Move 10<br>
<input type="radio" name="move10" value="r">Rock</input><br>
<input type="radio" name="move10" value="p">Paper</input><br>
<input type="radio" name="move10" value="s">Scissors</input><br>
<input type="submit" value="submit">

</form>
</div>





</div>






EOP



print<<EOP;



EOP


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