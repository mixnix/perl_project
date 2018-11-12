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
($id_from_cookie, $num_from_cookie)=split / /,$cookie;

#print "@lines";
$html_string = "jestem html string";
$array_index = 0;
foreach $line(@lines){
   ($id, $id_number)=split / /,$line,2;
   $cookie_hash{$id}=$id_number;
   if($id_number == $id_from_cookie && $id == $num_from_cookie){
     $html_string = "znaleziono ciastko";
	 last;

   }
   $array_index = $array_index + 1;
}

splice @lines, $array_index, 1;

open(OUT, ">$cookie_file") || die "can write to $cookie_file";
print OUT "@lines";
close OUT;

if ($cookie && ($cookie_hash{$id_from_cookie}==$num_from_cookie)){


print header();
print start_html();
print "$html_string<br>";
print "logging out successful ";
print "$array_index @lines <br>";
#print "$id_from_cookie $num_from_cookie<br>";
print "<br>";
print "<a href='index.cgi'>main page</a>";
}else{

print header();
print start_html();
print "error";
print "<br>";
print "<a href='index.cgi'>main page</a>";

}
