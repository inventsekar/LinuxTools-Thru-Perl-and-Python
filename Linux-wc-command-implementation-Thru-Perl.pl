#!/usr/bin/perl -w
# invent sekar  - 3/5/2014 - wednesday
# Perl implementation of Linux wc command, using a while loop and of course, the great regex ;).

print "Please enter line1:\n";
my $line1=<STDIN>;
chomp $line1;

$line2="A quiet bubble floating on a sea of noise. - The god of small things - Arundhati Roy";
$line3="Hello how are you";

################################
# Finding number of words: wc -w
#################################
print "Finding numer of words: wc -w\n";
print "---------------------------------\n";
$nWords=0;

while ($line1 =~ /\b\w+\b/g){ $nWords++; }
print "line1 is $line1\n";
print "\$line1 contains $nWords words\n";

$nWords=0;
while ($line2 =~ /\b\w+\b/g){ $nWords++; }
print "line2 is $line2\n";
print "\$line2 contains $nWords words\n";

$nWords=0;
while ($line3 =~ /\b\w+\b/g){ $nWords++; }
print "line3 is $line3\n";
print "\$line3 contains $nWords words\n\n";

################################
# Finding number of characters: wc -m
#################################
print "Finding numer of characters : wc -m\n";
print "---------------------------------\n";

$nChar=0;
while($line1 =~ /./g){$nChar++;}
print "line1 is $line1\n";
print "\$line1 contains $nChar characters\n";

$nChar=0;
while($line2 =~ /./g){$nChar++;}
print "line2 is $line2\n";
print "\$line2 contains $nChar characters\n";

$nChar=0;
while($line3 =~ /./g){$nChar++;}
print "line3 is $line3\n";
print "\$line3 contains $nChar characters\n";

A Sample Run:
# ./wc-for-loop-test.pl
Please enter line1:
hiiiiiiii
Finding numer of words: wc -w
---------------------------------
line1 is hiiiiiiii
$line1 contains 1 words
line2 is A quiet bubble floating on a sea of noise. - The god of small things - Arundhati Roy
$line2 contains 16 words
line3 is Hello how are you
$line3 contains 4 words

Finding numer of characters : wc -m
---------------------------------
line1 is hiiiiiiii
$line1 contains 9 characters
line2 is A quiet bubble floating on a sea of noise. - The god of small things - Arundhati Roy
$line2 contains 84 characters
line3 is Hello how are you
$line3 contains 17 characters
