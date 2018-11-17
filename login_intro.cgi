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
print "<a href='index.cgi'>main page</a>";
}else{


print<<EOP; 


<!DOCTYPE html>
<html>
<head><title>RPS login</title>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

</head>
<body>
<div class="container" style="padding:20px">
      <div class="jumbotron">
         <h1 class="display-4">Login Page</h1>
         <hr class="my-4">
      </div>
      

<h2>Login</h2>
<form action="login.cgi" method="post">
<p><label for="id_username">Username:</label> <input type="text" name="id" autofocus required id="id_username"></p>
<p><label for="id_password">Password:</label> <input type="password" name="password" required id="id_password"></p>
<button class="btn btn-success ml-2" type=”submit”>Login</button>
</form>
</body>
</html>

EOP
}
