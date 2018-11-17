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

$cookie= cookie('random-name');
($num_from_cookie, $id_from_cookie)=split / /,$cookie;

#print "@lines";
$html_string = "jestem html string";
$array_index = 0;
foreach $line(@lines){
   ($id, $id_number)=split / /,$line,2;
   $cookie_hash{$id}=$id_number;
   if($id_number == $num_from_cookie && $id == $id_from_cookie){
     $html_string = "znaleziono ciastko";
	 last;

   }
   $array_index = $array_index + 1;
}

splice @lines, $array_index, 1;

open(OUT, ">$cookie_file") || die "can write to $cookie_file";
print OUT "@lines";
close OUT;

print header();
print start_html();

if ($cookie && $cookie_hash{$id_from_cookie} && ($cookie_hash{$id_from_cookie}==$num_from_cookie)){

print<<EOP;

<head><title>Logout confirmation</title>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

</head>

<body>s
 <div class="container" style="padding:20px">
      <div class="jumbotron">
         <h1 class="display-4">Logout Confirmation</h1>
        <p class="lead">
logging out successfull
        </p>
         <hr class="my-4">
      </div>

<form action="index.cgi" method="post">
<button class="btn btn-success ml-2" type=”submit”>Back to main page</button>
</form>
</body>
</html>


EOP

}else{

print "error";
print "<br>";
print "<a href='index.cgi'>main page</a>";

}
