#!/usr/bin/perl -w

# Prompt for first name, last name and phone number.
# - if missing input, display error message.
# - otherwise, display confirmation message.

use CGI qw(:standard -debug);
use CGI::Carp qw(fatalsToBrowser);


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

<head><title>Registration</title></head>
<body>
<hr><h1>Registration</h1><hr>

$html_string




<hr>
<form action="index.html">
 <input type="submit" value="Back to main page">
 </form>
</body>
</html>

EOP


