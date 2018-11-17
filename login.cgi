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
if ($cookie && $cookie_hash{id_from_cookie} && ($cookie_hash{$id_from_cookie}==$num_from_cookie)){

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
@all_passwords = ();


$id = param("id");
$password = param("password");
if($id eq "" or $password eq ""){
 die("username or password is empty, go back and try again");

}
 $html_string = "password or username is incorrect, try again";

foreach $line(@lines){
  @words_in_line = split / /, $line;
  $temporary_password = $words_in_line[1];
  chomp $temporary_password;
  if ( $id eq $words_in_line[0] && $password eq $temporary_password){
    $html_string = "id and pass and password are correct";
    #load all cookies from file
$cookie_file = "cookie.txt";
if (!-e $cookie_file){
  print header();
  print h2("$cookie_file doesn't exist.");
  exit;
}else{
    open(IN,"$cookie_file") || die "cant read $cookie_file";
  while(<IN>){
       chomp;
     my($id_2,$num_2)=split/ /;
     $cookie_hash{$id_2}=$num_2;
  }
  close IN;
}


#create cookie
$cookie_id = int(rand(1000000));
$cookie_hash{$id}=$cookie_id;

$cookie = cookie(
  -name => "random-name",
  -value => "$cookie_id $id",
);

#save cookie data to file
open(OUT, ">$cookie_file") || die "cant write to $cookie_file";
foreach $ida(sort keys %cookie_hash){
   print OUT "$ida $cookie_hash{$ida}\n";
}
close OUT;

  }
}




#sent cookie to user's computer
print header(-cookie=>$cookie,-charset=>'utf-8');

print<<EOP; 

<head><title>Login confirmation</title>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

</head>
<body>








 <div class="container" style="padding:20px">
      <div class="jumbotron">
         <h1 class="display-4">Login Confirmation</h1>
        <p class="lead">

EOP

print ("$html_string");

print<<EOP;


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
