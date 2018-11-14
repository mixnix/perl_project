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
print "<h1>pick simple strategy</h1><br>";
print "<p>here you can pick simple strategy that you want to play against</p>";
$simple_strategies = "simple_strategies.txt";
open(INS, "$simple_strategies") || die "cant read $simple_strategies";
@s_lines=<INS>;
close INS;
print("<form action='play_simple_strategy.cgi' method='post'>");
foreach $line(@s_lines){
   ($s_name, $the_rest)=split / /,$line,2;
   print("<input type='radio' name='s_name' value='$s_name'>$s_name</input><br>");
}
print("<input type='submit' value='submit'>");

print("</form>");

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
