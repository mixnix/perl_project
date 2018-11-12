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
($id_from_cookie, $num_from_cookie)=split / /,$cookie;
if ($cookie && ($cookie_hash{$id_from_cookie}==$num_from_cookie)){

print header();
print start_html();
print "you are already logged in";
print "<br>";
print "<a href='index.cgi'>main page</a>";
}else{


print<<EOP; 


<!DOCTYPE html>
<html>
<head><title>RPS login</title>
</head>
<body>
<h3>RPS login</h3>

<form action="login.cgi" method="post">


<br>
userID
<input type="text" name="id"></input><br>
password
<input type="password" name="password"></input><br>
<br>
<input type="submit" value="submit">

</form>
</body>
</html>

EOP
}
