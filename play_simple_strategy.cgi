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
print "<h1>here you play vs picked strategy</h1><br>";
$s_name = param("s_name");
print "<p>strategy name: $s_name</p>";

#open file with strategies and loads all line
#for through all lines and check for containing of straegy name
#when you find good line then use split to split it into 10 different arugments

#show form with 10 radio buttons that you have to pick move and then submit
#create new page that shows you your score, there you will load strategy and check which round were win. 1 point for win 0.5 point for draw and 0 points for losing round

#from there you can only go back
#that shall be enough for today
#after taht spend one day on implementing bootstrap and check how it looks
#show it to professor on monday

print("<form action='play_simple_strategy_confirm.cgi' method='post'>");
print("Name<br>");
print("<input type='text' name='s_name' value='$s_name' readonly><br>");
print<<EOP;


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

EOP

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
