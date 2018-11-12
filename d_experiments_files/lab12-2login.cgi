#!/usr/bin/perl -w


use CGI qw(:standard -debug);
use CGI::Carp qw(fatalsToBrowser);

use utf8;
use Encode;

$id = param("nick");
$password = param("password");


#load all ids to array
#so later we can just check for zawieranie
$file = "logins";
open(INF,"$file") || die("cant open $file for checking if id exists");
@lines = <INF>;
close(INF);

#load all ids and passwordsd into array from array of lines 
@all_ids = ();
@all_pass = ();

foreach $line(@lines){
  @words_in_line = split / /, $line;
  push(@all_ids,@words_in_line[0]);
  $temp_pass = @words_in_line[1];
  chomp $temp_pass;
  push(@all_pass,$temp_pass);

}



#check if id exists
#and check if passwords matches
$html_string = "";
$index_id=-1;
#print("nick: $id <br>");
#print("all_ids: @all_ids <br>");
#print("$all_ids[0] <br>");
if ( $id ~~ @all_ids ){
  foreach ([0..@all_ids]){
  	  #print("index: $_ wartosc: $all_ids[$_]");
      if($all_ids[$_] eq $id)
	  {
	  	$index_id=$_;
		last;
	  }
  }
  if ( $all_pass[$index_id] eq $password ){
	$html_string = "password is correct";
  }else{
    $html_string = "password is incorrect";
  }
  
}else{
$html_string = "Your id ($id) doesn't exists please go back and try again.";
}

#create cookie
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

$cookie_id = int(rand(1000000));
$cookie_hash{$id}=$cookie_id;

$cookie = cookie(
	-name => "random-name",
	-value => "$cookie_id $id",
);

open(OUT, ">$cookie_file") || die "cant write to $cookie_file";
foreach $ida(sort keys %cookie_hash){
   print OUT "$ida $cookie_hash{$ida}\n";
}
close OUT;
print header(-cookie=>$cookie,-charset=>'utf-8');
print start_html("Login");

print "$html_string";
print "<br>";
print "Welcome $id";
print "<br>";
print "<br>";
print "<a href='confirm-cookie.cgi'>see cookie</a>";


print end_html();
											



