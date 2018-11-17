#!/usr/bin/perl -w

# Prompt for first name, last name and phone number.
# - if missing input, display error message.
# - otherwise, display confirmation message.

use CGI qw(:standard -debug);
use CGI::Carp qw(fatalsToBrowser);

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

#load all ids to array
#so later we can just check for zawieranie
$file = "logins";
open(INF,"$file") || die("cant open $file for checking if id exists");
@lines = <INF>;
close(INF);

#print $lines[0];

@all_ids = ();


$id = param("id");
$password = param("password");

foreach $line(@lines){
  @words_in_line = split / /, $line;
  push(@all_ids,@words_in_line[0]);
  }


$html_string = "";
if ( $id ~~ @all_ids ){
$html_string = "$id already exists, go back and try again";
}else{
open(OUTF, ">>$file") || die("cant open $file for writing id there");
print OUTF "$id $password\n";
close(OUTF);
$html_string = "Thank you for registration. Your account ($id) has been created.";
}


print header();

print<<EOP; 

<head><title>Registration</title>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">


</head>
<body>
<div class="container" style="padding:20px">
      <div class="jumbotron">
         <h1 class="display-4">Registration Confirmation</h1>
        <p class="lead">


$html_string

        </p>
         <hr class="my-4">
      </div>

<form action="index.cgi" method="post">
<button class="btn btn-success ml-2" type=”submit”>Back to main page</button>
</form>
</body>
</html>









EOP

}
