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
print header();
print start_html("register intro");

my %cookie_hash;
#print "@lines";
foreach $line(@lines){
   ($id, $id_number)=split / /,$line,2;
   $cookie_hash{$id}=$id_number;
}

$cookie= cookie('random-name');
($num_from_cookie, $id_from_cookie)=split / /,$cookie;
if(exists $cookie_hash{$id_from_cookie}){
$thing_in_hash = exists $cookie_hash{$id_from_cookie};
print "checks if that thing in hash exists: $thing_in_hash<br>";
}
$rownosc_hash = $cookie_hash{$id_from_cookie} == $num_from_cookie;
if ($cookie && (exists $cookie_hash{$id_from_cookie}) && ($cookie_hash{$id_from_cookie}==$num_from_cookie)){

print "you are already logged in";
print "<br>";
print "<a href='index.cgi'>main page</a>";
}else{

print<<EOP;

<body>
<h3>RPS register form</h3>

<form action="register.cgi" method="post">


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
