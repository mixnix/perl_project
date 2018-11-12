#!/usr/bin/perl -w


use CGI qw(:standard -debug);
use CGI::Carp qw(fatalsToBrowser);

print header();
print start_html();

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
print "got your cookie: $cookie";

}else {
print "something didnt work";
print "<br>";
print "$cookie";
print "<br>";
print "$cookie_hash{$id_from_cookie} $num_from_cookie";
print "end of text";

}
